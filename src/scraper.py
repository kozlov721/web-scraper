from typing import Final

import chromedriver_autoinstaller
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils import Property

URL: Final[str] = 'https://www.sreality.cz/en/search/for-sale/apartments'


def download_page() -> BeautifulSoup:
    chromedriver_autoinstaller.install()

    options: Options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    with webdriver.Chrome(options=options) as driver:
        driver.get(URL)
        driver.delete_cookie('per_page')
        driver.add_cookie({
            'name': 'per_page',
            'value': '500',
            'domain': 'www.sreality.cz'
        })
        driver.refresh()

        try:
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'name'))
            )
        except TimeoutError:
            raise TimeoutError('Timeout when waiting for page refresh.')

        return BeautifulSoup(driver.page_source, 'html.parser')


def scrape() -> list[Property]:
    soup: BeautifulSoup = download_page()
    props: list[Property] = []
    for prop in soup.find_all(class_='property'):
        props.append({
            'name': prop.find(class_='name').text,
            'locality': prop.find(class_='locality').text,
            'img': prop.find('img').attrs['src'],
            'url':
                f'https://www.sreality.cz/{prop.find(class_="title")["href"]}',
        })
    return props

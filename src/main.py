from typing import Final

from database import save_to_db
from html_gen import generate_page
from scraper import scrape
from server import start_server
from utils import Property

HOSTNAME: Final[str] = '0.0.0.0'
PORT: Final[int] = 8080


if __name__ == '__main__':
    props = scrape()
    save_to_db(props)
    generate_page()
    start_server(HOSTNAME, PORT)

from database import save_to_db
from scraper import scrape
from server import start_server
from utils import generate_page
from typing import Final


HOSTNAME: Final[str] = '0.0.0.0'
PORT: Final[int] = 8080


if __name__ == '__main__':
    props = scrape()
    save_to_db(props)
    generate_page(props)
    start_server(HOSTNAME, PORT)

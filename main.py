from database import save_to_db
from scraper import scrape
from server import start_server
from utils import generate_page


if __name__ == '__main__':
    props = scrape()
    save_to_db(props)
    generate_page(props)
    start_server()

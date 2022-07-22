import psycopg
from configparser import ConfigParser

from utils import Property


def read_config(filename: str = 'database.ini', section: str = 'postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')
    return db


def save_to_db(props: list[Property]) -> None:
    with psycopg.connect(**read_config()) as conn:
        with conn.cursor() as cur:
            cur.execute('''
                CREATE TABLE properties (
                    id serial PRIMARY KEY,
                    name text,
                    locality text,
                    img text,
                    url text
                )
            ''')
            for prop in props:
                cur.execute(
                    '''
                    INSERT INTO properties (name, locality, img, url)
                    VALUES (%s, %s, %s, %s)
                    ''',
                    (prop['name'], prop['locality'], prop['img'], prop['url'])
                )

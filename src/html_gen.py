import psycopg
from psycopg.rows import dict_row

from database import read_config
from utils import Property


def prop_to_html(prop: Property) -> str:
    return f'''
      <div>
        <h2>
          <a href="{prop['url']}">
            {prop['name']}
          </a>
        </h2>
        <h3>{prop['locality']}</h3>
        <img src="{prop['img']}" alt="{prop['locality']}">
      </div>
    '''


def generate_html() -> None:
    with psycopg.connect(**read_config()) as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute('SELECT name, locality, img, url FROM properties')

            props_html = ''.join(prop_to_html(prop) for prop in cur)
            html = f'''
              <!DOCTYPE html>
              <html lang="cs-cz">
                <head>
                  <meta charset="utf-8">
                  <title>apartments for sale</title>
                  <link rel="icon" href="data:,">
                  <style>
                    div {{border-bottom: 4px solid black}}
                  </style>
                </head>
                <body>
                  {props_html}
                </body>
              </html>
            '''

    with open('index.html', 'w') as file:
        file.write(html)

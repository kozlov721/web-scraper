Property = dict[str, str]


def prop_to_html(prop: Property) -> str:
    return f'''
      <div>
        <h2>{prop['name']}</h2>
        <h3>{prop['locality']}</h3>
        <img src="{prop['img']}" alt="{prop['locality']}">
      </div>
    '''


def generate_page(props: list[Property]) -> None:
    props_html = ''.join(prop_to_html(prop) for prop in props)
    html = f'''
      <!DOCTYPE html>
      <html lang="cs-cz">
        <head>
          <meta charset="utf-8">
          <title>apartments for sale</title>
          <link rel="icon" href="data:,">
        </head>
        <body>
          {props_html}
        </body>
      </html>
    '''

    with open('index.html', 'w') as file:
        file.write(html)

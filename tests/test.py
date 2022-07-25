import requests
from requests.exceptions import RequestException
from time import sleep

def test_number_results():
    while True:
        try:
            req = requests.get('http://127.0.0.1:8080')
            break
        except RequestException:
            sleep(1)

    assert req.content.count(b'<div>') == 500

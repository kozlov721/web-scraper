from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Final


HOSTNAME: Final[str] = '0.0.0.0'
PORT: Final[int] = 8080


class Server(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(200)
        if self.path == '/':
            self.path = '/index.html'
        with open(self.path[1:]) as index:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(index.read(), 'utf-8'))


def start_server():
    webServer = HTTPServer((HOSTNAME, PORT), Server)
    print(f'Server started at http://{HOSTNAME}:{PORT}')
    webServer.serve_forever()

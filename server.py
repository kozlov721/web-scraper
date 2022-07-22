from http.server import BaseHTTPRequestHandler, HTTPServer


class Server(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(200)
        if self.path == '/':
            self.path = '/index.html'
        with open(self.path[1:]) as index:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(bytes(index.read(), 'utf-8'))


def start_server(hostname: str, port: int):
    server = HTTPServer((hostname, port), Server)
    print(f'Starting server at http://127.0.0.1:{port}', flush=True)
    server.serve_forever()

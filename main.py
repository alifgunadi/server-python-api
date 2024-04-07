from http.server import HTTPServer, BaseHTTPRequestHandler
from utils import logger_setup

HOST = "192.168.1.210"
PORT = 4981
logger = logger_setup.setup_logger()


class NeuralHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(
            bytes("<html><body><h1>Judul Satu</h1></body></html>", "utf-8")
        )


server = HTTPServer((HOST, PORT), NeuralHTTP)
logger.info(f"Server is running at {server}")
print(f"Server is running at {HOST}:{PORT}")

server.serve_forever()
server.server_close()
print("Server stopped!")

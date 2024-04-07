from http.server import HTTPServer, BaseHTTPRequestHandler
import socket
from utils import logger_setup

HOST = "192.168.1.210"
PORT = 4981
logger = logger_setup.setup_logger()
socket.gethostname()


class NeuralHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        client_ip = self.client_address[0]
        user_agent = self.headers.get("User-Agent")
        logger.info(f"Request from {client_ip}. User-Agent: {user_agent}")

        self.wfile.write(
            bytes(
                f"<html><body><h1>Device information:</h1></br><p>Client information: {user_agent}</p><p>Client IP: {client_ip}</p></body></html>",
                "utf-8",
            )
        )


server = HTTPServer((HOST, PORT), NeuralHTTP)
logger.info(f"Server is running at {server}")
print(f"Server is running at {HOST}:{PORT}")

server.serve_forever()
server.server_close()
print("Server stopped!")

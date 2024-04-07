from flask import Flask, request, jsonify
from utils import logger_setup

app = Flask(__name__)
logger = logger_setup.setup_logger()


@app.route("/")
def do_GET():
    try:
        user_agent = request.headers["user-agent"]
        client_ip = request.remote_addr
        print(f"[CLIENT IP] {client_ip}")
        print(f"[CLIENT HEADER] {user_agent}")
        logger.info(f"[CLIENT] IP: {client_ip}, HEADER: {user_agent}")
        return (
            f"<html><body><h1>Device information:</h1></br><p>Client information: {user_agent}</p><p>Client IP: {client_ip}</p></body></html>",
            200,
        )
    except Exception as error:
        print(f"An error occurred: {str(error)}")
        return "An error occurred", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4432, debug=False)

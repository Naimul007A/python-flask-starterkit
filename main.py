from flask import Flask
from app.Controllers import register_all_blueprints
import atexit
import signal
import sys

from flask_cors import CORS

from app.Helpers.response_helper import success_response
import config.app as appConfig

app = Flask(__name__)

# Initialize CORS
CORS(app)

# Register shutdown handlers
# atexit.register()

def signal_handler(sig, frame):
    """Handle Ctrl+C and other signals"""
    print("\nShutting down gracefully...")
    sys.exit(0)


# Register signal handlers for graceful shutdown
signal.signal(signal.SIGINT, signal_handler)  # Ctrl+C
signal.signal(signal.SIGTERM, signal_handler)  # Termination


# Automatically register all blueprints from Controllers package
@app.route("/")
def index():
    return success_response("Welcome to the API")


register_all_blueprints(app)


if __name__ == "__main__":
    app.run(host=appConfig.HOST,port=appConfig.PORT,debug=appConfig.DEBUG)

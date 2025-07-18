from dotenv import load_dotenv
import os

load_dotenv()
# Main Config
HOST=os.getenv("HOST","localhost")
PORT=int(os.getenv("PORT",8000))
DEBUG=os.getenv("DEBUG","True").lower() in ("true", "1", "yes", "on")

# Database Config
DATABASE_URL=os.getenv("DATABASE_URL")

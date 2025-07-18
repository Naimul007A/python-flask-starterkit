from flask import Blueprint
from app.Services.home_service import HomeService

# Create a blueprint for home routes
home_bp = Blueprint("home", __name__)
home_service = HomeService()

@home_bp.route("/home")
def home():
    """
    Home route
    """
    return home_service.home()

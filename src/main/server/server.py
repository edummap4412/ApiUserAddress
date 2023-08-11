from flask import Flask
from src.main.router.routers import user_router_bp

app = Flask(__name__)

app.register_blueprint(user_router_bp)

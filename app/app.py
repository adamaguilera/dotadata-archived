from flask import Flask
from app.routes.dota2v2_route import dota2v2

# Start Flask App
app = Flask(__name__)

# Register blueprints
app.register_blueprint(dota2v2)

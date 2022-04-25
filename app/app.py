import os

from flask import Flask
from app.routes.dota2v2_route import dota2v2


# Setup CONFIG variables
ENV = os.getenv('ENV')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

# Start Flask App
app = Flask(__name__)

# Register blueprints
app.register_blueprint(dota2v2)

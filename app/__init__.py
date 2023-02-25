import code
from flask import Flask
import os

from .auth import auth
from app.db import init_db_command

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='NEVER_STOP_LEARNING',
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE') 
    )
    
    app.cli.add_command(init_db_command)
    
    app.register_blueprint(auth)
        
    return app
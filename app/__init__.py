from flask import Flask
import os

from .auth import auth
from .setting import setting
from app.db import init_db_command

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('FLASK_SECRET_KEY'),
        DATABASE_HOST=  os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=  os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=  os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=   os.environ.get('FLASK_DATABASE'),
        MAIL_SERVER = os.environ.get('FLASK_MAIL_SERVER'),
        MAIL_PORT = os.environ.get('FLASK_MAIL_PORT'),
        MAIL_USE_SSL = os.environ.get('FLASK_MAIL_USE_SSL'),
        MAIL_USE_TSL = os.environ.get('FLASK_MAIL_USE_TSL'),
        MAIL_USERNAME = os.environ.get('FLASK_MAIL_USERNAME'),
        MAIL_PASSWORD = os.environ.get('FLASK_MAIL_PASSWORD')
    )
    
    app.cli.add_command(init_db_command)
    
    app.register_blueprint(auth)
    app.register_blueprint(setting)
        
    return app
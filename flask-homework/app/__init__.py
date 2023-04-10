from flask import Flask
from logging.config import dictConfig
from config import AppConfig
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app.config.from_object(AppConfig)
app.secret_key = os.getenv('SECRET_KEY')
db.init_app(app)

from app.views import *
from app.models import *

with app.app_context():
    db.create_all()
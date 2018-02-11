from flask import Flask, g
import sqlite3
import os
from models import db
import logging

# configuration
DATABASE = os.path.join(os.path.dirname(__file__), 'alayatodo.db')
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False

#logging configuration
logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), 'alayatodo.log'), level=logging.ERROR,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

#initialize app
app = Flask(__name__)
app.config.from_object(__name__)

# initialize and create the database
db.init_app(app)
db.create_all(app=app)

import alayatodo.views
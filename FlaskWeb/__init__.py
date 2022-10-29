"""
The flask application package.
"""

from operator import imod
from flask import Flask
from config import AppConfig
import logging
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#init flask web application
app = Flask(__name__)
app.config.from_object(AppConfig)

# init logging of application
app.logger.setLevel(logging.INFO)
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.INFO)
app.logger.addHandler(streamHandler)

# config database
Session(app=app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWeb.views



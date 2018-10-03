"""Init application and set up all components and packages."""
import os
import sys

from flask import Flask
from flask_assets import Environment
from flask_htmlmin import HTMLMIN
import flask_login
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_sslify import SSLify


app = Flask(__name__)

app.config.from_object('brochure.config.Config')
app.secret_key = os.environ['CV_PASSWORD']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MINIFY_PAGE'] = True
app.config['ASSETS_DEBUG'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ['GMAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['GMAIL_PASSWORD']
app.config['AK_EMAIL'] = os.environ['AK_EMAIL']
app.config['CV_PASSWORD'] = os.environ['CV_PASSWORD']
app.config['GOOGLE_SITE_VERIFICATION_TOKEN'] = os.environ['GOOGLE_SITE_VERIFICATION_TOKEN']

db = SQLAlchemy(app)
assets = Environment(app)
mail = Mail(app)
sslify = SSLify(app)
login_manager = flask_login.LoginManager()

assets.init_app(app)
HTMLMIN(app)
login_manager.init_app(app)

from brochure.models.user import Users

sys.path.append('brochure')

from brochure.controllers import *

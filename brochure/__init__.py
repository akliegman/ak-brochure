"""Init application and set up all components and packages."""

from flask import Flask
from flask_assets import Environment
from flask_mail import Mail
from flask_htmlmin import HTMLMIN
from flask_sqlalchemy import SQLAlchemy
import sys
import os


app = Flask(__name__)

app.config.from_object('brochure.config.Config')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MINIFY_PAGE'] = True
app.config['ASSETS_DEBUG'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ['GMAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['GMAIL_PASSWORD']

db = SQLAlchemy(app)
assets = Environment(app)
mail = Mail(app)

assets.init_app(app)
HTMLMIN(app)


from brochure.models.user import User

sys.path.append('brochure')


from brochure.controllers import *

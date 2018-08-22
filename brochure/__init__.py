from flask import Flask
from flask_assets import Bundle, Environment
from flask_htmlmin import HTMLMIN
from flask_sqlalchemy import SQLAlchemy
import sys


app = Flask(__name__)

app.config.from_object('brochure.config.Config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MINIFY_PAGE'] = True
app.config['ASSETS_DEBUG'] = False

db = SQLAlchemy(app)
assets = Environment(app)

assets.init_app(app)
HTMLMIN(app)

from brochure.models.user import User

sys.path.append('brochure')
from brochure.controllers import *

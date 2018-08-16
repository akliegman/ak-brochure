from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys
app = Flask(__name__)

app.config.from_object('brochure.config.Config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from brochure.models.user import User

sys.path.append('brochure')
from brochure.controllers import *

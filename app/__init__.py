from flask import Flask
from config import Config

# import flask lib for sql
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# this is for Config file
app.config.from_object(Config)

# db setup
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from app import routes


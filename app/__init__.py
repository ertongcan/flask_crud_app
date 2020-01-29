from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
print(Config.SECRET_KEY)

db = SQLAlchemy(app)
# SET FLASK_DEBUG=1
# SET FLASK_APP=wayfairPortal.py
from app import routes, models

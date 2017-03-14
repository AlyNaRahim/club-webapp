import os
from flask import Flask
# from config import basedir

app = Flask(__name__)
# app.config.from_object('config')
app.secret_key = 'secret key'

from app import views, models


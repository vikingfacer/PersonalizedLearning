from flask import Flask
from peewee import SqliteDatabase

import config

app = Flask(__name__)
db = SqliteDatabase(config.DB_NAME)

from app.model.color import Color
from app.model.user import User

db.create_tables([
    User,
    Color
], safe=True)

from flask import Flask
from peewee import SqliteDatabase

import config

app = Flask(__name__)
db = SqliteDatabase(config.DB_NAME)

from app.model.color import Color
from app.model.user import User
from app.model.professor import Professor
from app.model.course import Course

db.create_tables([
    Color,
    User,
    Course,
    Professor
], safe=True)


# from app.controller.question import question

# app.register_blueprint(question)

from flask import Flask
from peewee import MySQLDatabase

import config

app = Flask(__name__)
db = MySQLDatabase(
    database=config.DB_NAME, host=config.DB_LOCATION, port=config.DB_PORT,
    user=config.DB_USERNAME, passwd=config.DB_PASSWORD)

from app.model.color import Color
from app.model.user import User
from app.model.professor import Professor
from app.model.course import Course
from app.model.questions import Question

db.create_tables([
    Color,
    User,
    Course,
    Professor,
    Question
], safe=True)


from app.controller.question import question
app.register_blueprint(question)

from app.controller.user import user
app.register_blueprint(user)

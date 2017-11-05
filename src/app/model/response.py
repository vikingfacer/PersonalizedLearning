from peewee import *

from app import db
from app.model.questions import Question


class Response(Model):
    content = CharField()
    question_id = ForeignKeyField(Question, to_field='id', related_name='response')

    class Meta:
        database = db

    def __str__(self):
        return "<Response>"

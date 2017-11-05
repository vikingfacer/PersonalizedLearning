import json
from peewee import *

from app import db
from app.model.questions import Question


class Response(Model):
    content = CharField()
    question_id = ForeignKeyField(Question, to_field='id', related_name='response')

    class Meta:
        database = db

    def __str__(self):
        return json.dumps(self.__dict__["_data"])

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        JsonData = dict()
        JsonData.update(self.__dict__["_data"])
        JsonData.update(self.__dict__["_obj_cache"])
        return JsonData

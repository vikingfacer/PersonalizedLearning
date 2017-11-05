import json
from peewee import *

from app import db


class Question(Model):
    """docstring for Questions"""
    content = TextField()
    test_type = TextField()
    group = TextField()

    def __str__(self):
        return json.dumps(self.__dict__["_data"])

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return self.__dict__["_data"]

    class Meta:
        database = db

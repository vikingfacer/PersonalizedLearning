from peewee import *
from flask_login import UserMixin
import json

from app import db
from app.model.color import Color


class User(Model, UserMixin):
    name = CharField()
    password = CharField()
    email = CharField(unique=True)
    color_id = ForeignKeyField(Color, to_field='id', related_name='user', null=True)

    def __str__(self):
        return json.dumps(self.__dict__["_data"])

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        JsonData = dict()
        JsonData.update(self.__dict__["_data"])
        JsonData.update(self.__dict__["_obj_cache"])
        return JsonData

    class Meta:
        database = db
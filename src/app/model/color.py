from peewee import *

from app import db
import json 

class Color(Model):
    color_value = CharField(6)

    class Meta:
        database = db

    def __str__(self):
        return json.dumps(self.__dict__["_data"])

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return self.__dict__["_data"]

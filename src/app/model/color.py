from peewee import *

from app import db


class Color(Model):
    color_value = CharField(6)

    class Meta:
        database = db

    def __str__(self):
        return "<Color>"

    def __repr__(self):
        return "<Color>"

    def to_dict(self):
        return self.__dict__["_data"]

from peewee import *

from app import db


class Color(Model):
    color_value = CharField(6)

    class Meta:
        database = db

    def __str__(self):
        return "<Color>"

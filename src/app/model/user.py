from peewee import *
from flask_login import UserMixin

from app import db
from app.model.color import Color


class User(Model, UserMixin):
    name = CharField()
    password = CharField()
    email = CharField(unique=True)
    color_id = ForeignKeyField(Color, to_field='id', related_name='user')

    class Meta:
        database = db

    def __str__(self):
        return "<User>"

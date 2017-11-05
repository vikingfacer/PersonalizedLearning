from peewee import *

from app import db


class Question(Model):
    """docstring for Questions"""
    content = TextField()
    test_type = TextField()
    group = TextField()

    def __str__(self):
        return "<Question>"

    def __repr__(self):
        return "<Question>"

    class Meta:
        database = db

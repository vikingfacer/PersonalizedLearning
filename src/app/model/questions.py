from peewee import *

from app import db

class Question(Model):
    """docstring for Questions"""
    content = textField()
    test_type = textField()
    group = textField()

    def __str__(self):
        return "<Question>"

    def __repr__(self):
    return "<Question>"
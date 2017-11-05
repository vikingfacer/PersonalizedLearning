from peewee import *

from app import db
from app.model.professor import Professor


class Course(Model):
    title = CharField()
    professor_id = ForeignKeyField(Professor, to_field='id', related_name='course')
    subject = CharField()

    class Meta:
        database = db

    def __str__(self):
        return "<course>"

    def to_dict(self):
        return self.__dict__["_data"]

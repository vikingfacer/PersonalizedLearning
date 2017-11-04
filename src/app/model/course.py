from peewee import *

from app import db
from app.model.color import Color

class course(Model):
	title = CharField()
	color_id = ForeignKeyField(Color, to_field='id', related_name='course')


    def __str__(self):
        return "<course>"
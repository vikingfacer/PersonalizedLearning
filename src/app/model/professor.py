from peewee import *

from app import db
from app.model.color import Color

class Professor(Model):
	name = CharField()
	color_id = ForeignKeyField(Color, to_field='id', related_name='professor')


	def __str__(self):
		return "<professor>"
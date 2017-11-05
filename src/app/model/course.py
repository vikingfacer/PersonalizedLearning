from peewee import *

from app import db
from app.model.color import Color

class Course(Model):
	title = CharField()
	professor_id = ForeignKeyField(Professor, to_field='id', related_name='course')
	subject = CharField()

	def __str__(self):
	
		return "<course>"

	def to_dict(self):
		return self.__dict__["_data"]

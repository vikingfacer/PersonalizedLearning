from peewee import *

from app import db


class Question(Model):
    """docstring for Questions"""
    content = TextField()
    test_type = TextField()
    group = TextField()

    def __str__(self):
        return json.dumps(self.__dict__["_data"])

    def __repr__(self):
<<<<<<< HEAD
        return self.__str__()

    def to_dict(self):
        return self.__dict__["_data"]

=======
        return "<Question>"
>>>>>>> 2e735d2bf2218c619b6619e651a075600a93ac80

    class Meta:
        database = db

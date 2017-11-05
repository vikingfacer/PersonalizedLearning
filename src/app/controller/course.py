import json

from peewee import DoesNotExist
from flask import Blueprint, request, Response

from app.model.course import course

course = Blueprint('course', __name__)


@course.route('/course/<subject>')
def course_search(subject):
	return json.dumps(
        [course.to_dict() for course in course.select().where(course.title == subject)]
    )
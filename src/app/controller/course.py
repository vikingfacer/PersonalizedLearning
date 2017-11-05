import json

from flask import Blueprint

from app.model.course import Course

course = Blueprint('course', __name__)


@course.route('/course/<subject>')
def course_search(subject):
    return json.dumps(
        [course.to_dict() for course in Course.select().where(Course.subject == subject)]
    )

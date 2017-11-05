import json

from peewee import DoesNotExist
from flask import Blueprint, request, Response

from app.core.mbti import MBTI
from app.model.user import User
from app.model.questions import Question


question = Blueprint('question', __name__)


@question.route('/mbti/questions')
def fetch_mbti_questionnaire():
    return json.dumps(
        [question.to_dict() for question in Question.select()]
    )


@question.route('/mbti/questionnaire/<userid>', methods=['POST'])
def questionnaire_results(userid):
    mbti_results = MBTI(request.form.lists())

    try:
        user = User.get(User.id == userid)
    except DoesNotExist:
        return Response(status=404)

    return json.dumps(
        {
            "mbti_value": mbti_results.mbti_value,
            "color": mbti_results.color
        }
    )

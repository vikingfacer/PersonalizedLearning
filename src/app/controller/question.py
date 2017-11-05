import json

from peewee import DoesNotExist
from flask import Blueprint, request, Response

from app.core.mbti import MBTI
from app.model.user import User


question = Blueprint('question', __name__)


# TODO: Use actual model
class Question():

    def __dict__(self):
        return {
            "question": "What is your name"
        }

    @staticmethod
    def get_mbti():
        questions = [Question(), Question(), Question()]

        return [obj.__dict__() for obj in questions]


@question.route('/mbti/questions')
def fetch_mbti_questionnaire():
    return json.dumps(
        Question.get_mbti()
    )


@question.route('/mbti/questionnaire/<userid>', methods=['POST'])
def questionnarie_results(userid):
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

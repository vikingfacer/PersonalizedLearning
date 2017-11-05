import json

from peewee import DoesNotExist
from flask import Blueprint, request, Response

from app.core.mbti import MBTI
from app.core.kva import KVA
from app.model.user import User
from app.model.questions import Question
from app.model.answer import Answer


question = Blueprint('question', __name__)


@question.route('/questions')
def fetch_questionnaire():
    return json.dumps(
        [question.to_dict() for question in Question.select()]
    )


@question.route('/questions/mbti')
def fetch_mbti_questionnaire():
    return json.dumps(
        [question.to_dict() for question in Question.select().where(Question.test_type == "MBTI")]
    )


@question.route('/questions/lp')
def fetch_lp_questionnaire():
    lp_questions = [question.to_dict() for question in Question.select().where(Question.test_type == "LP")]

    for question in lp_questions:
        question["answers"] = [
            answer.to_dict() for answer in Answer.select().where(Answer.question_id == question["id"])
        ]
    return json.dumps(lp_questions)


@question.route('/questions/mbti/<userid>', methods=['POST'])
def questionnaire_mbti_results(userid):
    mbti_results = MBTI(request.form.lists())

    try:
        user = User.get(User.id == userid)
    except DoesNotExist:
        return Response(status=404)

    user.mbti_color_id = mbti_results.color
    user.mbti_value = mbti_results.mbti_key
    user.save()

    return json.dumps(
        {
            "mbti_value": mbti_results.mbti_value,
            "color": mbti_results.color
        }
    )


@question.route('/questions/lp/<userid>', methods=['POST'])
def questionnaire_lp_results(userid):
    KVA_results = KVA(request.form.lists())

    try:
        user = User.get(User.id == userid)
    except DoesNotExist:
        return Response(status=404)

    user.lp_color_id = KVA_results.color
    user.lp_value = KVA_results.key
    user.save()

    return json.dumps(
        {
            "lp_value": KVA_results.color,
            "color": KVA_results.color
        }
    )
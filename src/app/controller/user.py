import json

from peewee import DoesNotExist
from flask import Blueprint, request, Response

from app.model.user import User


user = Blueprint('user', __name__)


@user.route('/login', methods=['POST'])
def login_user():
    try:
        current_user = User.get(User.email == request.form.get("email"))
    except DoesNotExist:
        return Response(status=401)

    if current_user.password == request.form.get("password"):
        user_dict = current_user.to_dict()
        user_dict.pop("password")
        return Response(json.dumps(user_dict), status=200, mimetype='json/type')
    else:
        return Response(status=401)


@user.route('/user', methods=['POST'])
def create_user():
    new_user = User()
    new_user.name = request.form.get("name")
    new_user.email = request.form.get("email")
    new_user.password = request.form.get("password")
    new_user.color_id = None

    new_user.save()

    return Response(status=200)


@user.route('/user/<userid>', methods=['GET'])
def get_user(userid):
    try:
        new_user = User.get(User.id == userid)
    except DoesNotExist:
        return Response(status=404)

    return json.dumps(new_user.to_dict())

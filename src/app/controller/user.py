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
        return Response(status=404)

    if current_user.password == request.form.get("password"):
        return Response(status=200)


@user.route('/user', methods=['POST'])
def create_user():
    new_user = User()
    new_user.name = request.form.get("name")
    new_user.email = request.form.get("email")
    new_user.password = request.form.get("password")
    new_user.color_id = None

    new_user.save()

    return Response(status=200)

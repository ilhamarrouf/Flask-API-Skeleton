"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 18/04/20
    :time: 09.59
"""

from app import db
from app.models.user import User
from app.requests.user import UserRequest
from app.utils.response import respond_json, respond_json_with_validation_errors
from flask import abort, Blueprint, request, jsonify, url_for
from werkzeug.exceptions import BadRequest

mod = Blueprint("user_controller", __name__, url_prefix="/api")


@mod.route("/users", methods=["GET"])
def index():
    return respond_json(
        success=True,
        message=None,
        data=[user.serialize for user in User.query.all()]
    )


@mod.route("/users", methods=["POST"])
def store():
    form = UserRequest(request.form)

    if not form.validate():
        return respond_json_with_validation_errors(form.errors)

    user = User(username=form.username.data)
    user.hash_password(form.password.data)

    try:
        db.session.add(user)
        db.session.commit()
    except Exception as exception:
        db.session.rollback()

        return respond_json(
            success=False,
            message=getattr(exception, 'message', repr(exception)),
            data=None,
            code=BadRequest.code
        )

    return respond_json(
        success=True,
        message="successfully added user",
        data=user.serialize,
        code=200
    )
"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 18/05/20
    :time: 19.45
"""

from app import jwt
from app.utils.response import respond_json
from werkzeug.exceptions import Unauthorized


@jwt.invalid_token_loader
def invalid_token_loader(callback):
    return respond_json(
        success=False,
        message='unauthenticated.',
        code=Unauthorized.code
    )


@jwt.unauthorized_loader
def unauthorized_loader(callback):
    return respond_json(
        success=False,
        message='unauthenticated.',
        code=Unauthorized.code
    )


@jwt.expired_token_loader
def expired_token_loader():
    return respond_json(
        success=False,
        message='Token has expired.',
        code=Unauthorized.code
    )
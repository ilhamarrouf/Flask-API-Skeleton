"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 18/05/20
    :time: 19.43
"""

from app import app
from app.exceptions.authentication_http_exception import AuthenticationHttpException
from app.utils.response import respond_json
from werkzeug.exceptions import (
    BadRequest, NotFound, InternalServerError,
    TooManyRequests, MethodNotAllowed,
    Unauthorized
)


@app.errorhandler(BadRequest.code)
def bad_request(error):
    return respond_json(
        message="Error 400: Bad request",
        success=False,
        code=BadRequest.code,
    )


@app.errorhandler(Unauthorized.code)
def unauthenticated(error):
    return respond_json(
        message="Error 401: Unauthenticated",
        success=False,
        code=BadRequest.code,
    )


@app.errorhandler(NotFound.code)
def not_found(error):
    return respond_json(
        message="Error 404: Not found",
        success=False,
        code=NotFound.code,
    )


@app.errorhandler(MethodNotAllowed.code)
def method_not_allowed(error):
    return respond_json(
        message="Error 405: Method not allowed",
        success=False,
        code=MethodNotAllowed.code,
    )


@app.errorhandler(TooManyRequests.code)
def too_many_request(error):
    return respond_json(
        message="429 Too Many Requests",
        success=False,
        code=TooManyRequests.code,
    )


@app.errorhandler(InternalServerError.code)
def internal_server_error(error):
    return respond_json(
        message="Error 500: Internal server error",
        success=False,
        code=InternalServerError.code,
    )


@app.errorhandler(AuthenticationHttpException)
def handle_authentication_http_exception(error):
    return respond_json(
        success=False,
        code=error.status_code,
        message=error.message,
        errors=error.errors
    )
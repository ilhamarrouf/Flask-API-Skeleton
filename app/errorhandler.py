"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 19/04/20
    :time: 12.14
"""

from app import app
from app.utils.response import respond_json
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError, TooManyRequests


@app.errorhandler(BadRequest.code)
def bad_request(error):
    return respond_json(
        message="Error 400: Bad request",
        success=False,
        data=None,
        code=BadRequest.code,
    )


@app.errorhandler(NotFound.code)
def not_found(error):
    return respond_json(
        message="Error 404: Not found",
        success=False,
        data=None,
        code=NotFound.code,
    )


@app.errorhandler(TooManyRequests.code)
def too_many_request(error):
    return respond_json(
        message="429 Too Many Requests",
        success=False,
        data=None,
        code=TooManyRequests.code,
    )


@app.errorhandler(InternalServerError.code)
def internal_server_error(error):
    return respond_json(
        message="Error 500: Internal server error",
        success=False,
        data=None,
        code=InternalServerError.code,
    )

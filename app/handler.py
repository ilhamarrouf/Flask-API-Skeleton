"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 19/04/20
    :time: 12.14
"""
import logging
from app import app
from app.utils.helpers import storage_path
from app.utils.response import respond_json
from datetime import datetime
from logging.handlers import RotatingFileHandler
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


def log_handler():
    handler = RotatingFileHandler(
        storage_path(f"logs/{datetime.today().strftime('%Y-%m-%d')}.log"),
        maxBytes=10000,
        backupCount=1
    )
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter(
        f'[%(asctime)s] {app.config["ENV"]}.%(levelname)s: %(message)s'
    ))

    return handler

app.logger.addHandler(log_handler())
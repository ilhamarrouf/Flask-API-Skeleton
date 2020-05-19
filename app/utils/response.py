"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 18/04/20
    :time: 08.32
"""

from flask import request, jsonify
from werkzeug.exceptions import UnprocessableEntity


def respond_json(success, message=None, data=None, meta=None, code=200):
    response = {"success": success}

    if message:
        response["message"] = message

    if data:
        response["data"] = data

    if meta:
        response['meta'] = meta

    return jsonify(response), code


def respond_json_with_validation_errors(errors):
    return jsonify({
        "success": False,
        "message": "The given data was invalid.",
        "errors": errors,
    }), UnprocessableEntity.code

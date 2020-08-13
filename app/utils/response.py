"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 18/04/20
    :time: 08.32
"""

from flask import request, jsonify
from werkzeug.exceptions import UnprocessableEntity


def respond_json(success, message=None, data=None, meta=None, errors=None, code=200):
    response = {"success": success}

    if not message is None:
        response["message"] = message

    if not data is None:
        response["data"] = data

    if not meta is None:
        response['meta'] = meta

    if not errors is None:
        response['errors'] = errors

    return jsonify(response), code


def respond_json_with_validation_errors(errors):
    return jsonify({
        "success": False,
        "message": "The given data was invalid.",
        "errors": errors,
    }), UnprocessableEntity.code

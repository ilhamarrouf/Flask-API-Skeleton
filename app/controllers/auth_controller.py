"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 17/05/20
    :time: 18.43
"""
from cerberus import Validator
from flask import jsonify, request
from flask.blueprints import Blueprint
from app.exceptions.authentication_http_exception import AuthenticationHttpException
from app.models.user import User
from flask_jwt_extended import jwt_required, current_user
from app.utils.response import respond_json, respond_json_with_validation_errors

mod = Blueprint('auth_controller', __name__, url_prefix='/api/auth')


@mod.route('/login', methods=['POST'])
def login():
    """
    Validate request
    """
    validator = Validator({
        'username': {
            'type': 'string',
            'required': True,
            'minlength': 5,
            'maxlength': 32,
        },
        'password': {
            'type': 'string',
            'required': True,
            'minlength': 5,
            'maxlength': 32,
        }
    })

    if not validator.validate(request.json):
        return respond_json_with_validation_errors(validator.errors)

    """
    Get data user by username
    """
    user = User.query.filter_by(
        username=request.json.get('username')
    ).first()

    if not user:
        raise AuthenticationHttpException

    if not user.verify_password(request.json.get('password')):
        raise AuthenticationHttpException

    """
    Response to json
    """
    return jsonify({
        "token_type": "Bearer",
        "access_token": user.create_access_token(),
    })


@mod.route('/account', methods=['GET'])
@jwt_required
def account():
    return respond_json(
        success=True,
        data=current_user.serialize
    )
"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 17/05/20
    :time: 18.43
"""

from flask import jsonify, request
from flask.blueprints import Blueprint
from werkzeug.exceptions import Unauthorized
from app.models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.utils.response import respond_json

mod = Blueprint('auth_controller', __name__, url_prefix='/api/auth')


@mod.route('/login', methods=['POST'])
def login():
    user = User.query.filter_by(
        username=request.json.get('username', None)
    ).first()

    if not user:
        return jsonify({
            'success': False,
            'message': 'These credentials do not match our records.',
            'errors': {'username': ['These credentials do not match our records.']}
        }), Unauthorized.code

    if not user.verify_password(request.json.get('password', None)):
        return jsonify({
            'success': False,
            'message': 'These credentials do not match our records.',
            'errors': {'username': ['These credentials do not match our records.']}
        }), Unauthorized.code

    return jsonify({
        "token_type": "Bearer",
        "access_token": user.create_access_token(),
    })


@mod.route('/account', methods=['GET'])
@jwt_required
def account():
    return respond_json(
        success=True,
        data=User.query.get(get_jwt_identity()).serialize
    )
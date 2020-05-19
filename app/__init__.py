#!/usr/bin/env python

"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 18/04/20
    :time: 08.26
"""

import os
from flask_jwt_extended.jwt_manager import JWTManager
from flask_mail import Mail
from flask_rq2 import RQ
from app.utils.storage import Minio
from flask import Flask, jsonify, request
from flask_caching import Cache
from flask_cors.extension import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_sqlalchemy import SQLAlchemy
from flasgger.base import Swagger

# Initialize core objects

app = Flask(__name__)
app.config.from_object("config")

cache = Cache(app)
cors = CORS(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=[
        "100 per minute",
        "5 per second"
    ],
)
mail = Mail(app)
swagger = Swagger(app)
storage = Minio(app)
rq = RQ(app)

# -- Handler
from app.handlers import (
    http_handler,
    jwt_handler,
    log_handler
)


# -- Models
from app.models import (
    user,
    role,
    role_user
)

# Comment above code when change database systems
if not os.path.exists("db.sqlite"):
    db.create_all()


# -- Controllers
from app.controllers import (
    auth_controller,
    file_controller,
    homepage_controller,
    mail_controller,
    user_controller
)

app.register_blueprint(auth_controller.mod)
app.register_blueprint(file_controller.mod)
app.register_blueprint(homepage_controller.mod)
app.register_blueprint(mail_controller.mod)
app.register_blueprint(user_controller.mod)



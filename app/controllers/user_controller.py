"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 18/04/20
    :time: 09.59
"""

from app.models.user import User
from app.utils import paginator
from app.utils.response import respond_json
from flask import Blueprint, request
from sqlalchemy.sql.expression import desc


mod = Blueprint("user_controller", __name__, url_prefix="/api")


@mod.route("/users", methods=["GET"])
def index():
    users = User.query.order_by(desc(User.username)).paginate(
        page=request.args.get('page', type=int, default=1),
        per_page=request.args.get('per_page', type=int, default=15),
    )

    return respond_json(
        success=True,
        message=None,
        data=[user.serialize for user in users.items],
        meta={
            'pagination': paginator.paginate(users)
        }
    )

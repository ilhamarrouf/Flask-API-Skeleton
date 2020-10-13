"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 03/05/20
    :time: 12.10
"""

from flask import abort
from flask_sqlalchemy import Pagination
from werkzeug.exceptions import BadRequest


def paginate(paginator):
    if isinstance(paginator, Pagination):
        return {
            'has_next': paginator.has_next,
            'has_prev': paginator.has_prev,
            'next_num': paginator.next_num,
            'prev_num': paginator.prev_num,
            'page': paginator.page,
            'pages': paginator.pages,
            'per_page': paginator.per_page,
            'total': paginator.total,
        }

    """
    Abort request when paginator not instance sqlalchemy pagination
    """
    abort(BadRequest.code)
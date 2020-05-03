"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 03/05/20
    :time: 00.35
"""

from app import rq
from app.utils import log
from flask import current_app


@rq.job('high', timeout=60)
def perform(n):
    for x in range(10):
        log.telegram(__name__ + f'@success({n}), index: {x}')
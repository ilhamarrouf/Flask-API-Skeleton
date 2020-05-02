"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 03/05/20
    :time: 00.35
"""

from app import rq
from app.utils import log


@rq.job
def perform():
    log.telegram(__name__+'@success')
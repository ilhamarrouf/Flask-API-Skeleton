"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 06/05/20
    :time: 05.14
"""

from app import app, rq


if __name__ == '__main__':
    rq.get_worker().work(burst=app.config['RQ_BURST'])
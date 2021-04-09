"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 18/05/20
    :time: 19.46
"""

import logging
from app import app
from app.utils.helpers import storage_path
from datetime import datetime
from logging.handlers import RotatingFileHandler


def log_handler():
    handler = RotatingFileHandler(
        storage_path(f"logs/{datetime.today().strftime('%Y-%m-%d')}.log"),
        maxBytes=10000,
        backupCount=1
    )
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter(
        f'[%(asctime)s] {app.config["ENV"]}.%(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))

    return handler


app.logger.addHandler(log_handler())
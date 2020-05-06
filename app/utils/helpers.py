"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 26/04/20
    :time: 11.00
"""

import os
from app import app


def base_path(path=''):
    if path:
        path = '/'+path

    return os.path.dirname(app.instance_path)+path

def storage_path(path=''):
    if path:
        path = '/'+path

    return os.path.dirname(app.instance_path)+'/storage'+path
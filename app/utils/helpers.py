"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 26/04/20
    :time: 11.00
"""

import os
from flask import current_app, _app_ctx_stack


def base_path(path=''):
    if path:
        path = '/'+path

    return os.path.dirname(current_app.instance_path)+path

def storage_path(path=''):
    if path:
        path = '/'+path

    return os.path.dirname(current_app.instance_path)+'/storage'+path
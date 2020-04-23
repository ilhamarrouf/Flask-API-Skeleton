"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 23/04/20
    :time: 20.36
"""

from app import storage
from app.utils.response import respond_json
from flask import request
from flask.blueprints import Blueprint

mod = Blueprint("file_controller", __name__, url_prefix='/api')


@mod.route('/files', methods=['POST'])
def store():
    file = storage.put('my_files', request.files['file'])

    return respond_json(
        success=True,
        message='Successfully upload files',
        data={
            "file": storage.temporary_url(file),
        },
        code=200
    )
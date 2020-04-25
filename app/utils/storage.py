"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 19/04/20
    :time: 14.18
"""

import minio
import os
from app.utils import string
from flask import current_app, _app_ctx_stack
from werkzeug.utils import secure_filename


class Minio(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    # Initialize lib with config app
    def init_app(self, app):
        app.config.setdefault('MINIO_ENDPOINT', 'play.minio.io:9000')
        app.config.setdefault('MINIO_ACCESS_KEY', 'secretacess')
        app.config.setdefault('MINIO_SECRET_KEY', 'secretkey')
        app.config.setdefault('MINIO_BUCKET', 'my_bucket')
        app.config.setdefault('MINIO_SECURE', True)
        app.config.setdefault('MINIO_REGION', None)
        app.config.setdefault('MINIO_HTTP_CLIENT', None)
        app.teardown_appcontext(self.teardown)

    # Make connection
    def connect(self):
        return minio.Minio(
            current_app.config['MINIO_ENDPOINT'],
            access_key=current_app.config['MINIO_ACCESS_KEY'],
            secret_key=current_app.config['MINIO_SECRET_KEY'],
            secure=current_app.config['MINIO_SECURE'],
            region=current_app.config['MINIO_REGION'],
            http_client=current_app.config['MINIO_HTTP_CLIENT']
        )

    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'minio'):
            ctx.minio._http.clear()

    def put(self, path, file_stream):
        try:
            # Split file
            attributes = file_stream.filename.split('.')
            file_name = secure_filename(string._random(32) + '_' + attributes[0] + '.' + attributes[1])
            file_path = path + '/' + file_name

            # save to /tmp
            file_stream.save("/tmp/"+file_name)

            # store file to object storage
            self.connection.fput_object(
                current_app.config['MINIO_BUCKET'],
                file_path,
                "/tmp/"+file_name,
                content_type=file_stream.content_type
            )

            # remove file from /tmp
            os.remove("/tmp/"+file_name)

            # return with filename
            return file_path
        except Exception as err:
            current_app.logger.error(getattr(err, 'message', repr(err)))

    def temporary_url(self, file_path):
        try:
            return self.connection.presigned_get_object(
                current_app.config['MINIO_BUCKET'],
                file_path
            )
        except Exception as err:
            current_app.logger.error(getattr(err, 'message', repr(err)))

    @property
    def connection(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'minio'):
                ctx.minio = self.connect()
            return ctx.minio

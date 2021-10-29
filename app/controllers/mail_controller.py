"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 11/05/20
    :time: 22.19
"""

from flask import abort
from flask.blueprints import Blueprint
from flask_mail import Message
from werkzeug.exceptions import BadRequest
from app import app, mail
from app.utils.response import respond_json

mod = Blueprint('mail_controller', __name__, url_prefix='/api/mails')


@mod.route('/send', methods=['POST'])
def send():
    try:
        # please read docs https://pythonhosted.org/Flask-Mail/
        message = Message('Hello this is my subject mail')
        message.recipients = ['ilham.arrouf@gmail.com', ]
        message.html = 'Hello my name is <b>ilhamarrouf</b>'

        with app.app_context():
            mail.send(message)

        return respond_json(
            success=True,
            message='Successfully send mail...'
        )
    except Exception as err:
        app.logger.error(getattr(err, 'message', repr(err)))
        abort(BadRequest.code)

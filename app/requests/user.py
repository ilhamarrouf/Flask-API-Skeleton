"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 18/04/20
    :time: 13.53
"""


from app.models.user import User
from wtforms import Form, PasswordField, StringField, validators
from wtforms.validators import ValidationError


def username_exists(form, field):
    if User.query.filter_by(username=field.data).first():
        raise ValidationError('The username has already been taken.')


class UserRequest(Form):
    username = StringField('username', [
        validators.DataRequired(),
        validators.Length(min=4, max=32),
        validators.Regexp(r'^[\w.@+-]+$', message='space characters are prohibited'),
        username_exists,
    ])

    password = PasswordField('password', [
        validators.DataRequired(),
        validators.Length(min=5, max=64),
        validators.Regexp(r'^[\w.@+-]+$', message='space characters are prohibited'),
    ])

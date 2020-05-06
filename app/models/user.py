"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 18/04/20
    :time: 08.30
"""

from app import app, db
from app.models.role import Role
from app.models.role_user import role_user
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from passlib.apps import custom_app_context


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    password = db.Column(db.String)

    roles = db.relationship(Role, secondary=role_user, lazy='subquery')

    def hash_password(self, password):
        self.password = custom_app_context.encrypt(password)

    def verify_password(self, password):
        return custom_app_context.verify(password, self.password)

    def generate_auth_token(self, expires_in=600):
        serializer = Serializer(app.config['SECRET_KEY'], expires_in=expires_in)

        return serializer.dumps({
            'id': self.id,
        })

    @property
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            'roles': [role.serialize for role in self.roles]
        }

    @staticmethod
    def verify_auth_token(token):
        serializer = Serializer(app.config['SECRET_KEY'])
        try:
            data = serializer.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None

        user = User.query.get(data['id'])

        return user

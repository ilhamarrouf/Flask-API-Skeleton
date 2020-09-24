"""
    Created by PyCharm
    ~~~~~~~~~~~
    :author: ilhamarrouf
    :date: 18/04/20
    :time: 08.30
"""

from app import db
from app.models.role import Role
from app.models.role_user import role_user
from passlib.hash import bcrypt
from flask_jwt_extended import create_access_token


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    password = db.Column(db.String)

    roles = db.relationship(Role, secondary=role_user, lazy='dynamic')

    def hash_password(self, password) -> str:
        self.password = bcrypt.hash(password)
        return self.password

    def verify_password(self, password) -> bool:
        return bcrypt.verify(password, self.password)

    def create_access_token(self, fresh=False):
        return create_access_token(
            identity=self.id,
            fresh=fresh
        )

    @property
    def serialize(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            'roles': [role.serialize for role in self.roles],
        }
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


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    password = db.Column(db.String)

    roles = db.relationship(Role, secondary=role_user, lazy='subquery')

    def hash_password(self, password):
        self.password = bcrypt.hash(password)
        return self.password

    def verify_password(self, password):
        return bcrypt.verify(password, self.password)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            'roles': [role.serialize for role in self.roles],
        }
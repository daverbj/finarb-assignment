from marshmallow import Schema, fields, pre_load, validate
from . import db, ma
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False, unique=True)
    def __init__(self, name):
        self.name = name


class UserSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
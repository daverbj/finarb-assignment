from marshmallow import Schema, fields, pre_load, validate
from . import db, ma
from .aadhar import AadharSchema
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    aadhar_info = db.relationship('Aadhar', back_populates="user")
    def __init__(self, name, password):
        self.name = name
        self.password = password
class UserSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    aadhar_info = fields.Nested(AadharSchema, many=True, only=('aadharNumber'))
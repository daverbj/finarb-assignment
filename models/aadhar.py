from marshmallow import Schema, fields, pre_load, validate
from . import db, ma
class Aadhar(db.Model):
    __tablename__ = 'aadhar'
    id = db.Column(db.Integer, primary_key=True)
    aadharNumber = db.Column(db.String(250), nullable=False, unique=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('aadhar', lazy='dynamic' ))

    def __init__(self, aadharNumber, userId):
        self.aadharNumber = aadharNumber
        self.userId = userId
class AadharSchema(ma.Schema):
    id = fields.Integer()
    userId = fields.Integer(required=True)
    aadharNumber = fields.String(required=True)
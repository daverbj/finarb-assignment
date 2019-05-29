from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required
from models import db
class AadharResource(Resource):
    @jwt_required
    def get(self, id=None):
        return {
            'answer': 42
        },200
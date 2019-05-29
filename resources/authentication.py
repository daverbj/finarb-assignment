from flask_restful import Resource
from flask import request
from models.user import User, UserSchema
from models import db
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
users_schema = UserSchema(many=True)
user_schema = UserSchema()

class AuthenticationResource(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        current_user = User.query.filter_by(
            name=json_data['username'], password=json_data['password']).first()
        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(json_data['username'])}, 404
        
        access_token = create_access_token(identity=current_user.id)
        refresh_token = create_refresh_token(identity=current_user.id)
        return {
            'message': 'Logged in as {}'.format(current_user.name),
            'access_token': access_token,
            'refresh_token': refresh_token
        }, 200
    @jwt_refresh_token_required
    def put(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        return {'access_token': access_token}

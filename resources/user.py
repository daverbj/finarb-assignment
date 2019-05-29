from flask_restful import Resource
from flask import request
from models.user import User, UserSchema
from models import db
users_schema = UserSchema(many=True)
user_schema = UserSchema()
class UserResource(Resource):
    def get(self, id=None):
        if id is None:
            users  = User.query.all()
            users = users_schema.dump(users).data
            return {'status': 'success', 'data': users}, 200
        else:
            user = User.query.get(id)
            if user:
                result = user_schema.dump(user).data  
                return { "status": 'success', 'data': result }, 200
            else:
                return { "status": 'not found' }, 404
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        if User.query.filter_by(name=json_data['username']).first():
          return {'message': 'User {} already exists'. format(json_data['username'])}, 400
        user = User(name=json_data['username'], password=json_data['password'])
        db.session.add(user)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush() 
            return { "status": 'fail' }, 400
        result = user_schema.dump(user).data  
        return { "status": 'success', 'data': result }, 200

            
        
        
       


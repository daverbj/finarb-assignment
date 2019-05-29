from flask_restful import Resource
from models.user import User, UserSchema
from models import db
users_schema = UserSchema(many=True)
user_schema = UserSchema()
class HelloWorld(Resource):
    def get(self):
        users  = User.query.all()
        users = users_schema.dump(users).data
        return {'status': 'success', 'data': users}, 200
    def post(self):
        user = User(name='abcd')
        db.session.add(user)
        db.session.commit()

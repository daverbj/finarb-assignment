from app import api
from resources.user import UserResource
api.add_resource(UserResource, '/users', endpoint="users")
api.add_resource(UserResource, '/users/<id>', endpoint="user")

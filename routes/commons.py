from app import api
from resources.user import UserResource
from resources.aadhar import AadharListResource
api.add_resource(UserResource, '/users', endpoint="users")
api.add_resource(UserResource, '/users/<id>', endpoint="user")
api.add_resource(AadharListResource, '/aadhars', endpoint="aadhars")


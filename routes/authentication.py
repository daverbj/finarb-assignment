from app import api
from resources.authentication import AuthenticationResource
api.add_resource(AuthenticationResource, '/login', endpoint="login")
api.add_resource(AuthenticationResource, '/logout', endpoint="logout")
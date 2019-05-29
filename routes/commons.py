from app import api
from resources.hello import HelloWorld
api.add_resource(HelloWorld, '/hello')

from app import api
from resources.aadhar import AadharResource
api.add_resource(AadharResource, '/aadhar', endpoint="aadhar")
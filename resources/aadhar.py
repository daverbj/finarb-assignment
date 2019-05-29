from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db
from models.aadhar import Aadhar, AadharSchema
from models.user import User, UserSchema
aadharSchema = AadharSchema()
class AadharResource(Resource):
    @jwt_required
    def get(self, id):
        authIdentity = get_jwt_identity()
        if (int(id) != authIdentity):
            return {"message": "Unauthorized Access"}, 403
        aadhar = Aadhar.query.filter_by(userId=int(id)).first()
        if aadhar:
            result = aadharSchema.dump(aadhar).data
            return {"message": "Aadher found", "data": result}, 200
        else:
            return {"message": "Aadher not found"}, 404
    @jwt_required
    def post(self, id):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400        
        authIdentity = get_jwt_identity()
        if (int(id) != authIdentity):
            return {"message": "Unauthorized Access"}, 403
        user = User.query.get(int(id))
        if user:
            aadhar = Aadhar(json_data['aadhar_number'], int(id))
            db.session.add(aadhar)
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                db.session.flush() 
                return { "status": 'fail' }, 400
            result = aadharSchema.dump(aadhar).data
            return {"message": "aadhar updated", "data":result}, 200
        else:
            return {"message": "user not found"}, 404
    @jwt_required
    def put(self, id):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400        
        authIdentity = get_jwt_identity()
        if (int(id) != authIdentity):
            return {"message": "Unauthorized Access"}, 403
        user = User.query.get(int(id))
        if user:
            aadhar = Aadhar.query.filter_by(userId=int(id)).first()
            aadhar.aadharNumber = json_data['aadhar_number']
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                db.session.flush() 
                return { "status": 'fail' }, 400
            result = aadharSchema.dump(aadhar).data
            return {"message": "aadhar updated", "data":result}, 200
        else:
            return {"message": "user not found"}, 404
from cloud_db.schemas import UserSchema
from cloud_db.models import User
from flask import request
from flask_restful import Resource
from database import Session
import os

class Signup(Resource):
    def post(self):
        user_schema = UserSchema()
        user_schema_dump = user_schema.dump(request.get_json())
        if user_schema_dump["password"] == user_schema_dump["password_verify"]:
             try:
                del user_schema_dump["password_verify"]
                new_user = User(**user_schema_dump)
                new_user.hash_password()
                session = Session()
                session.add(new_user)
                session.commit()

                newpath = f'/files-cloud/{new_user.username}'
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                
                return {'status': 'success',
                    'message': 'Successfully registered.'
                }, 201
             except:
                return {
                    'status': 'fail',
                    'message':  'Some error occurred. Please try again.'
                }, 401
        else:
            return {
                    'status': 'fail',
                    'message':  'Check that passwords are the same'
                }, 400
       
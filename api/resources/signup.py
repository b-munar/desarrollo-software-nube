from schemas import UserSchema
from models import User
from flask import request
from flask_restful import Resource
from db import db
import os

class Signup(Resource):
    def post(self):
        user_schema = UserSchema()
        user_schema_dump = user_schema.dump(request.get_json())
        try:
            new_user = User(**user_schema_dump)
            new_user.hash_password()
            db.session.add(new_user)
            db.session.commit()

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


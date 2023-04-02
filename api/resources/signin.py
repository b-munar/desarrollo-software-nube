import jwt
from datetime import datetime, timedelta
from schemas import UserSchema
from config import Config
from models import User
from flask import request
from flask_restful import Resource

class Signin(Resource):
    def post(self):
        user_schema = UserSchema()
        user_schema_dump = user_schema.dump(request.get_json())
        try:
            user = User.query.filter_by(username=user_schema_dump['username']).first()
            if user.check_password(user_schema_dump['password']):
                auth_token = jwt.encode({
                            'user_id': user.id,
                            'exp' : datetime.utcnow() + timedelta(minutes = 30)
                        }, Config.SECRET_KEY, algorithm="HS256")
                return {'status': 'success',
                        'message': 'Successfully logged in.',
                        'auth_token': auth_token
                    }, 200
            else:
                raise Exception()

        except:
            return {
                'status': 'fail',
                'message': 'Try again'
            }, 500

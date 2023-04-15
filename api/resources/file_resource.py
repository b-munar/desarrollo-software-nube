from flask_restful import Resource

from db import db
from utils import authenticate
from models import File, User
from flask import send_from_directory

class File(Resource):
    method_decorators = [authenticate]
    def get(self, filename, **kwargs):
        return send_from_directory(f'/files-cloud/{kwargs["user"].username}/', filename, as_attachment=True)
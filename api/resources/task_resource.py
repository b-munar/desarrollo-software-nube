from db import db
from models import Task as TaskModel, File
import base64
import json
from flask import request
from flask_restful import Resource
from utils import authenticate

from models import db , Task, TaskSchema

task_schema = TaskSchema()

class Task(Resource):
    method_decorators = [authenticate]
    def post(self, **kwargs):
        with open(request.json.get('path'), "rb") as file_path:
            file_binary = base64.b64encode(file_path.read())
        new_file = File(path=request.json.get('path'), binary=file_binary, user_id=kwargs["user"].id)
        db.session.add(new_file)
        db.session.flush()
        new_task = TaskModel(file_id=new_file.id, user_id=kwargs["user"].id, type_task=1)
        db.session.add(new_task)
        db.session.commit()
        return "hi"
    
    method_decorators = [authenticate]
    def get(self,**kwargs):  
             tasks = Task.query.all()
             tasks_json = [task_schema.dump(tasks) for task in tasks]
             return tasks_json
    

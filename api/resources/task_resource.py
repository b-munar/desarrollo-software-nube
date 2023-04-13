from db import db
from models import Task as TaskModel, File
import base64
from flask import request
from flask_restful import Resource
from utils import authenticate
from schemas.task_schema import TaskSchema
from models.task import TypeTask

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
    

class Tasks(Resource):
    method_decorators = [authenticate]
    def get(self, id_task, **kwargs):
        task = TaskModel.query.get_or_404(id_task)
        task.type_task = TypeTask(task.type_task)
        return task_schema.dump(task)


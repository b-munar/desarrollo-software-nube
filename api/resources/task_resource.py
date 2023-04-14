from flask import request
from flask_restful import Resource

from db import db
from utils import authenticate
from schemas import TaskSchema
from models import Task as TaskModel, File, TypeTask

task_schema = TaskSchema()

class Tasks(Resource):
    method_decorators = [authenticate]
    def post(self, **kwargs):
        request_file = request.files.get('file')
        file_name = request_file.filename
        file_path = f'/files-cloud/{kwargs["user"].username}/{file_name}'

        request_file.save(file_path)
        
        new_file = File(path=file_path, name=file_name, user_id=kwargs["user"].id)
        db.session.add(new_file)
        db.session.flush()

        new_format = TypeTask[request.form.to_dict()["new_format"]]
        new_task = TaskModel(file_id=new_file.id, user_id=kwargs["user"].id, type_task=new_format)
        db.session.add(new_task)
        db.session.commit()
        return task_schema.dump(new_task)
    
    def get(self,**kwargs):  
        maxReq = request.args.get("max", None)
        order = int(request.args.get("order", 0))
        query = db.session.query(TaskModel).all()
        tasks_json = [task_schema.dump(task) for task in query]
        tasks_json.sort(key=lambda T: T['id'], reverse=order)
        if maxReq is not None: 
            maxReq = int(maxReq)
        return tasks_json[:maxReq]
                        

    
class Task(Resource):
    method_decorators = [authenticate]
    def get(self, id_task, **kwargs):
        task = TaskModel.query.get_or_404(id_task)
        return task_schema.dump(task)
    
    
    


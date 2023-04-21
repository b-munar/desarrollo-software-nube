from flask import request
from flask_restful import Resource
from datetime import datetime
from utils import authenticate
from cloud_db.schemas import TaskSchema
from cloud_db.models import Task as TaskModel, File, TypeTask
import os

task_schema = TaskSchema()

from database import Session
class Tasks(Resource):
    method_decorators = [authenticate]
    def post(self, **kwargs):
        request_file = request.files.get('file')
        file_name = request_file.filename
        file_dir = f'/files-cloud/{kwargs["user"].username}/{datetime.now()}'
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        file_path = f'{file_dir}/{file_name}'

        request_file.save(file_path)
        session = Session()
        new_file = File(path=file_path, dir=file_dir, name=file_name, user_id=kwargs["user"].id)
        session.add(new_file)
        session.flush()

        new_format = TypeTask[request.form.to_dict()["new_format"]]
        new_task = TaskModel(file_id=new_file.id, user_id=kwargs["user"].id, type_task=new_format)
        session.add(new_task)
        session.commit()
        return task_schema.dump(new_task)
    
    def get(self,**kwargs):  
        maxReq = request.args.get("max", None)
        order = int(request.args.get("order", 0))
        session = Session()
        query = session.query(TaskModel).all()
        session.close()
        tasks_json = [task_schema.dump(task) for task in query]
        tasks_json.sort(key=lambda T: T['id'], reverse=order)
        if maxReq is not None: 
            maxReq = int(maxReq)
        return tasks_json[:maxReq]
                        

    
class Task(Resource):
    method_decorators = [authenticate]
    def get(self, id_task, **kwargs):
        session = Session()
        task = session.query(TaskModel).get(id_task)
        session.close()
        return task_schema.dump(task)
    
    def delete(self, id_task, **kwargs):
        session = Session()
        task = session.query(TaskModel).get(id_task)
        schema = task_schema.dump(task)
        if schema['status']:
            file = session.query(File).get(schema['file_id'])
            if os.path.exists(file.path) and os.path.exists(file.path.rsplit('.', 1)[0] + '.' + str(schema['type_task']).lower()):
                os.remove(file.path)
                os.remove(file.path.rsplit('.', 1)[0] + '.' + str(schema['type_task']).lower())
                session.delete(task)
                session.delete(file)
                session.commit()
                return '', 204
            else:
                return 'No fue posible eliminar los archivos', 409

        return 'El estado de la tarea de conversion es No Disponible', 409
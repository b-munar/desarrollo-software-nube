from flask_restful import Resource
from utils import authenticate
from cloud_db.models import File as FileModel
from flask import send_from_directory
from cloud_db.schemas import TaskSchema
from database import Session
from utils.gcp_storage import download_file
from flask import Response

class File(Resource):
    method_decorators = [authenticate]
    def get(self, id_file, **kwargs):
        schema = TaskSchema()
        session = Session()
        file = session.query(FileModel).get(id_file)
        task = schema.dump(file.tasks[0])
        session.close()
        file_download, content_type = download_file(bucket_name="gropo-2-nube-2023", file_name=file.path, name=file.name)
        return Response(file_download,  mimetype=content_type)

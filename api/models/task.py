from enum import IntEnum
from datetime import datetime
from marshmallow import Schema
from db import db

class TypeTask(IntEnum):
    ZIP = 1
    TAR_GZ  = 2
    TAR_BZ2= 3

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_task = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean, default=False)
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow)
    file_id = db.Column(db.Integer, db.ForeignKey('file.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class TaskSchema(Schema):
    class Meta:
        model= Task
        load_instance = True

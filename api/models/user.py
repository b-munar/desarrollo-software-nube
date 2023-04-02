import bcrypt
from db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    files = db.relationship('File', backref='user')
    tasks = db.relationship('Task', backref='user')

    def hash_password(self):
        self.password =  bcrypt.hashpw( self.password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

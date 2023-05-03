from flask_restful import Resource

import os

class Ping(Resource):
    
    def get(self,**kwargs):  
        return  "pong"
                        
    
"""
Test implementation of a Restful API
"""
import os
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api =   Api(app)

class HelloWorld(Resource):
    """
    Test API Endpoint
    """
    def get(self):
        """
        Getter for hello world
        """

        data={"data": "Hallo, endgueltig klappt diese scheiss api mit dem richtigen Namen"}

        return data

class HelloEndpoint(Resource):
    """
    New Endpoint - CI / CD purpose
    """
    def get(self):
        """
        Getter for new Endpoint
        """
        data={"data": "Hi there from new Endpoint"}

        return data

api.add_resource(HelloWorld,'/hello')
api.add_resource(HelloEndpoint,'/endpoint')

if __name__=='__main__':
    cfg_port = os.getenv('PORT', "5000")
    app.run(host="0.0.0.0", port=cfg_port)#, debug=True)
#Test

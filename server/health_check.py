from flask import make_response
from flask_restful import Resource


class HealthCheck(Resource):

    @staticmethod
    def get():
        return make_response('OK')
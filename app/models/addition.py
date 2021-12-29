# Third-party Libraries
from flask_restful import Resource, reqparse

class Addition(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('a', required=True, location="args")
        parser.add_argument('b', required=True, location="args")
        args = parser.parse_args()  
        msg = ""
        try:
            a = float(args["a"])
            b = float(args["b"])
        except Exception as error_msg:
            return str(error_msg), 200
        else:
            return a + b, 200

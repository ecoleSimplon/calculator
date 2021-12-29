# Third-party libraries
from flask import Blueprint
import flask_restful as restful

# Local imports 
from app.models.addition import Addition
from app.models.division import Division
from app.models.multiplication import Multiplication
from app.models.subtraction import Subtraction

api_blueprint = Blueprint('api,', __name__)
api = restful.Api()

api.add_resource(Addition, '/addition') 
api.add_resource(Division, '/division')  
api.add_resource(Multiplication, '/multiplication')  
api.add_resource(Subtraction, '/subtraction') 

api.init_app(api_blueprint)

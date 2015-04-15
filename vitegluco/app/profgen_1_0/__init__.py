from flask import Blueprint
from flask.ext.restful import Api

profgen_api_blueprint = Blueprint('profgen', __name__)
profgen_api = Api(profgen_api_blueprint)

from twitter import Twitter
from facebook import Facebook

profgen_api.add_resource(Twitter, prefix='/twitter')
profgen_api.add_resource(Facebook, prefix='/facebook')

# -*- coding: utf-8 -*-
from flask import Blueprint
from flask.ext.restful import Api
from twitter import Twitter
from facebook import Facebook

profgen_api_blueprint = Blueprint('profgen_v1.0_blueprint', __name__)
profgen_api = Api(profgen_api_blueprint, prefix='/profgen/v1.0')

profgen_api.add_resource(Twitter, '/twitter')
profgen_api.add_resource(Facebook, '/facebook')


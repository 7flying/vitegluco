# -*- coding: utf-8 -*-
from flask import Blueprint
from flask.ext.restful import Api
from botmanage import Bot, Bots

botmanage_api_blueprint = Blueprint('botmanage_v1.0_blueprint', __name__)
botmanage_api = Api(botmanage_api_blueprint, prefix='/botmanage/v1.0')

botmanage_api.add_resource(Bot, '/bot')
botmanage_api.add_resource(Bots, '/bots')

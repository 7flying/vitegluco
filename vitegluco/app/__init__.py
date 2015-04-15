# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__, static_url_path='')
app.config.from_object('config')

from app.routes import index

from .profgen_1_0 import profgen_api as profgen_api_1_0_blueprint
app.register_blueprint(profgen_api_1_0_blueprint, url_prefix='/profgen/v1.0')

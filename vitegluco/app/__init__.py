# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__, static_url_path='')
app.config.from_object('config')

from routes import index
from .profgen_1_0 import profgen_api_blueprint as profgen_api_1_0_blueprint
from .botmanage_1_0 import botmanage_api_blueprint as bot_api_1_0_blueprint

app.register_blueprint(profgen_api_1_0_blueprint)
app.register_blueprint(bot_api_1_0_blueprint)

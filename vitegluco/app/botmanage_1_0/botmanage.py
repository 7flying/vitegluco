# -*- coding: utf-8 -*-
from flask import jsonify
from flask.ext.restful import Resource, reqparse

from app import manager

class Bot(Resource):

    def __init__(self):
        super(Bot, self).__init__()

class Bots(Resource):

    def __init__(self):
        super(Bots, self).__init__()

# -*- coding: utf-8 -*-
from py4j.java_gateway import JavaGateway

EMAIL_SERVICES = EMAIL_SERVICES = ('GMAIL', 'MAILCOM')

class Gateway(object):
    GATEWAY = None
    
    @staticmethod
    def generate_gateway():
        if Gateway.GATEWAY is None:
            Gateway.GATEWAY = JavaGateway(start_callback_server=True, auto_convert=True)
        return Gateway.GATEWAY

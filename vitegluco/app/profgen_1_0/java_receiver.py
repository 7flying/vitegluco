# -*- coding: utf-8 -*-

class CaptchaSolver(object):
    """Interacts with java classes, requests a captcha resolution"""

    def solveCaptcha(self, captchaUrl):
        print " ",captchaUrl
        user_input = raw_input(" captcha? > ")
        return user_input

    class Java:
        implements = ['com.sevenflying.profgen.PyCallCaptchaSolver']
        

class DataReceiver(object):
    """Interacts with java classes, receives messages."""

    def sendResults(self, results):
        print "received:", results

    class Java:
        implements = ['com.sevenflying.profgen.PyCallDataSender']

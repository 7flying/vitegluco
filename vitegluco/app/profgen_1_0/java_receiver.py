# -*- coding: utf-8 -*-

class JavaReceiver(object):
    """Interacts with java classes."""
    
    def sendResults(self, results):
        pass

    def solveCaptcha(self, captchaUrl):
        return ""

    class Java:
        implements = ['com.sevenflying.profgen.PythonCallable']

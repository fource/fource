import requests

class HttpClass(object):
    """docstring for HttpClass"""
    def __init__(self, request_params):
        super(HttpClass, self).__init__()
        self.http_params = request_params
        
    def requestGenerator(self):
        req_url = self.http_params['url']
        req_method = self.http_params['method']
        req_headers = self.http_params['headers']
        req_auth = self.http_params['auth']

    def getRequest(self):
        pass

    def postRequest(self):
        pass

    def putRequest(self):
        pass

    def delRequest(self):
        pass

    def requestController(self):
        pass
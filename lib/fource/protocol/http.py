import requests

class HttpClass(object):
    """
    Generate an HTTP Request. Accepts request parameters as params_dict during init.

    Accepted Parameters:
    HTTP URL as url - String
    HTTP Method as method - String
    HTTP Headers as headers - Dictionary
    HTTP Basic Auth as auth - Tuple
    Query String/POST Data/PUT Data as data - Dictionary
    Request Type in Accept Header as datatype - String

    Usage:
    from http import HttpClass
    params = {'url':'https://httpbin.org/get','method':'get'}
    reqobj = HttpClass(params)
    r = reqobj.requestGenerator()
    """

    def __init__(self, http_params):
        self.req_url = http_params.get('url')
        self.req_method = http_params.get('method')
        if self.req_method is None:
            self.req_method = 'get'
        self.req_headers = http_params.get('headers')
        if self.req_headers is None:
            self.req_headers = {}
        self.req_auth = http_params.get('auth')
        self.req_data = http_params.get('data')
        self.requestDataTypeGenerator(http_params.get('data_type'))
        self.result = None

    def requestDataTypeGenerator(self, datatype):
        data_to_accept = {'json':'application/json','xml':'application/xml'}
        if data_to_accept.get(datatype) is None:
            self.req_headers['Accept'] = data_to_accept.get('json')
        else:
            self.req_headers['Accept'] = data_to_accept.get(datatype)

    def execute(self):
        if self.req_method.lower() == 'get':
            self.getRequest()
        if self.req_method == 'post':
            self.postRequest()
        if self.req_method == 'put':
            self.putRequest()
        if self.req_method == 'delete':
            self.delRequest()
        return self.result

    def getRequest(self):
        if self.req_auth is None:
            r = requests.get(self.req_url,headers=self.req_headers,params=self.req_data)
        else:
            r = requests.get(self.req_url,headers=self.req_headers,params=self.req_data,auth=self.req_auth)
        self.result = {'status':r.status_code, 'request_headers':r.request.headers, 'url':r.url, 'response_headers':r.headers}

    def postRequest(self):
        if self.req_auth is None:
            r = requests.post(self.req_url,headers=self.req_headers,params=self.req_data)
        else:
            r = requests.post(self.req_url,headers=self.req_headers,params=self.req_data,auth=self.req_auth)
        self.result = {'status':r.status_code, 'request_headers':r.request.headers, 'url':r.url, 'response_headers':r.headers}

    def putRequest(self):
        if self.req_auth is None:
            r = requests.put(self.req_url,headers=self.req_headers,params=self.req_data)
        else:
            r = requests.put(self.req_url,headers=self.req_headers,params=self.req_data,auth=self.req_auth)
        self.result = {'status':r.status_code, 'request_headers':r.request.headers, 'url':r.url, 'response_headers':r.headers}

    def delRequest(self):
        if self.req_auth is None:
            r = requests.delete(self.req_url,headers=self.req_headers,params=self.req_data)
        else:
            r = requests.delete(self.req_url,headers=self.req_headers,params=self.req_data,auth=self.req_auth)
        self.result = {'status':r.status_code, 'request_headers':r.request.headers, 'url':r.url, 'response_headers':r.headers}

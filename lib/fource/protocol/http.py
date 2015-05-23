import requests, json

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
    r = reqobj.execute()
    """

    def __init__(self, http_params):
        self.req_url = http_params.get('url')
        self.req_method = http_params.get('method')
        if self.req_method is None:
            self.req_method = 'get'
        self.req_headers = {'Content-Type':'application/json'}
        if http_params.get('headers') is not None:
            self.req_headers.update(http_params.get('headers'))
        self.req_auth = http_params.get('auth')
        self.req_data = http_params.get('data')
        self.result = None

    def execute(self):
        if self.req_method.lower() == 'get':
            self.getRequest()
        if self.req_method.lower() == 'post':
            self.postRequest()
        if self.req_method.lower() == 'put':
            self.putRequest()
        if self.req_method.lower() == 'delete':
            self.delRequest()
        if self.req_method.lower() == 'patch':
            self.patchRequest()
        return self.result

    def getRequest(self):
        if self.req_auth is None:
            resp = requests.get(self.req_url,headers=self.req_headers,params=self.req_data)
        else:
            resp = requests.get(self.req_url,headers=self.req_headers,params=self.req_data,auth=self.req_auth)
        self.result = {
            'status_code':resp.status_code,
            'request_headers':resp.request.headers,
            'url':resp.url,
            'response_headers':resp.headers,
            'response': resp.text,
            'response_json': resp.json(),
        }

    def postRequest(self):
        if self.req_auth is None:
            resp = requests.post(self.req_url,headers=self.req_headers,json=self.req_data)
        else:
            resp = requests.post(self.req_url,headers=self.req_headers,json=self.req_data,auth=self.req_auth)
        self.result = {
            'status_code': resp.status_code,
            'request_headers': resp.request.headers,
            'url': resp.url,
            'response_headers': resp.headers,
            'response': resp.text,
            'response_json': resp.json(),
        }

    def validator(self,response,validation_dic):
        """
        Usage
        ======
        response -> result object
        validation_dic -> obtained from YAML file

        if validator(response,validation_dic):
            print "There is some wrong with API"
        else:
            print "Alright.Everything is OK
        """

        failed_cases = []
        for property in validation_dic.keys():
            if property == 'status_code':
                if not str(response['status_code']).startswith(str(validation_dic[property])[0]):
                    failed_cases.append(property)
            elif property == 'content-type':
                if response['response_headers']['content-type'] != validation_dic[property]:
                    failed_cases.append(property)
            else:
                if validation_dic[property] != response['response_headers'][property]:
                    failed_cases.append(property)

        if not failed_cases:
            return (True, 'Test successful')
        else:
            fail_message = "Test failed. Found errors: %s" % ', '.join(failed_cases)
            return (False, fail_message)

    def putRequest(self):
        if self.req_auth is None:
            resp = requests.put(self.req_url,headers=self.req_headers,data=self.req_data)
        else:
            resp = requests.put(self.req_url,headers=self.req_headers,data=self.req_data,auth=self.req_auth)
        self.result = {
            'status_code': resp.status_code,
            'request_headers': resp.request.headers,
            'url': resp.url,
            'response_headers': resp.headers,
            'response': resp.text,
            'response_json': resp.json(),
        }

    def patchRequest(self):
        patchdata = self.req_data
        self.req_data = json.dumps(patchdata)
        if self.req_auth is None:
            resp = requests.patch(self.req_url,headers=self.req_headers,data=self.req_data)
        else:
            resp = requests.patch(self.req_url,headers=self.req_headers,data=self.req_data,auth=self.req_auth)
        self.result = {
            'status_code': resp.status_code,
            'request_headers': resp.request.headers,
            'url': resp.url,
            'response_headers': resp.headers,
            'response': resp.text,
            'response_json': resp.json(),
        }

    def delRequest(self):
        if self.req_auth is None:
            resp = requests.delete(self.req_url,headers=self.req_headers)
        else:
            resp = requests.delete(self.req_url,headers=self.req_headers,params=self.req_data,auth=self.req_auth)
        self.result = {
            'status_code': resp.status_code,
            'request_headers': resp.request.headers,
            'url': resp.url,
            'response_headers': resp.headers,
            'response': resp.text,
        }

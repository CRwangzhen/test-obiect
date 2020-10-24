import  requests
import json
from config.moudler_log import logger1
logger1 = logger1()
class operator_request():
    def get(self,getUrl,getHeader,**kwargs):
        response = requests.get(url=getUrl, headers=getHeader)

        return  response
    def post(self,postUrl,postHeaders=None,postdata=None,**kwargs):
        postResponse = requests.post(url=postUrl, data=postdata, headers=postHeaders)

        return postResponse

    def request(self,requestMethod, requestUrl, paramsType, requestData=None, headers=None):
        if requestMethod.lower() == "post":
            if paramsType == "json":


                requestData = eval(requestData)
                json_requestData = json.dumps(requestData)
                json_headers = eval(headers)
                response = self.post(requestUrl,postHeaders = json_headers,postdata = json_requestData)

                return  response

            elif paramsType == "form":
                form_requestData = eval(requestData)
                form_headers = eval(headers)
                response = self.post(requestUrl, postHeaders=form_headers, postdata=form_requestData)

                return response

        elif requestMethod.lower() == "get":
            if paramsType == "url":
                logger1.applog_pen(requestMethod.lower())

                request_url = "%s%s" % (requestUrl, "" if requestData is None else  requestData)
                if headers!="":
                    headers=json.loads(headers)
                response = self.get(getUrl=request_url, getHeader=headers)

                return response
            elif paramsType == "params":
                response = self.get(url=requestUrl, params=requestData, headers=headers)
                return response
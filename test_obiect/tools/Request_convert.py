import json
import jsonpath
from config.moudler_log import logger1
logger1 = logger1()

depend ={}
class Convert_convert():
    def convertOp(self,body):
        logger1.applog_pen("开始通过$字符分割参数：********************")
        logger1.applog_pen(body)

        bodylist = body.split("$")
        print(bodylist)

        num = 0
        for odd_nuber in bodylist:
            logger1.applog_pen("开始通过奇数分割参数：%s" % odd_nuber)
            if num % 2 == 1:
                logger1.applog_pen("开始通过$字符分割参数：%s" %odd_nuber)
                logger1.applog_pen("找出depend字典里面的值的索引")

                print(odd_nuber.find("."))


                a = odd_nuber.find(".")

                b = odd_nuber[:a]
                logger1.applog_pen("找出depend字典里面的值的索引得值")
                logger1.applog_pen(a)
                print(b)

                varvalue = depend[b]
                logger1.applog_pen("找出depend字典里面的值:%s"%varvalue)

                varvalues = json.loads(varvalue)
                logger1.applog_pen("通过loads加载")

                path_object = odd_nuber[a+1:]
                print(path_object)

                varchuck = jsonpath.jsonpath(varvalues,expr = "$."+path_object)

                bodylist[num] = str(varchuck[0])
            num += 1
        new_vlues = "".join(bodylist)
        return  new_vlues




# # A = "{"userid":"$uservar.data[0].userid$","openid":"$uservar.data[0].openid$","productid":"$productvar.data[0].productid$"}"
# a = '{"token": "$loginvar.token$"}'
# c = '{"userid":$uservar.data[0].userid$,"openid":"$uservar.data[0].openid$","productid":$productvar.data[0].productid$}'
#
# Convert_convert().convertOp(c)

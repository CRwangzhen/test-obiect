#coding=utf-8
import pytest
from data.Excelopen import excelData
from tools.Request_convert import Convert_convert,depend
from data_quest import operator_request
from config.moudler_log import logger1
import jsonpath
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

# logging.config.fileConfig(r"C:\Users\10466\Desktop\新建文件夹\pytest_file\pytest_20201018\config\logging.config", encoding="utf-8")
# logger1 = logging.getLogger('applog')
logger1 = logger1()

class Test_Param:
    # alex = excelData().getExcel()
    # alex1 = copy.copy(alex)
    # print("sssssssssssssss", alex)

    @pytest.mark.parametrize("url, body, header, method, method_type,exceptvalue,jsonpathvalue,dependency",excelData().getExcel())
    def test_start(self,url, body, header, method, method_type,exceptvalue,jsonpathvalue,dependency):
        Convert = Convert_convert()
        body = "" if body is None else body
        header = ""if header is None else header
        body = Convert.convertOp(body) if body.find("$") >=0 else body
        header = Convert.convertOp(header)  if header.find("$") >=0 else header
        print("**************************************", body)
        print("************************************", header)

        logger1.applog_pen("=============================================================================================")
        logger1.applog_pen(method)
        logger1.applog_pen(url)
        logger1.applog_pen(method_type)
        logger1.applog_pen(body)
        logger1.applog_pen(header)
        logger1.applog_pen("*********************************************************************************************")






        response = operator_request().request(method,url,method_type,requestData =body,headers =header)

        logger1.applog_pen("开始通过参数关联,将返回数据储存在depend ")
        logger1.applog_pen(response.json())

        if len(dependency)>0 and dependency.find("/") < 0:
            depend[dependency] = response.content

        logger1.applog_pen("找出断言数据")
        logger1.applog_pen(depend)
        assert_vlues = jsonpath.jsonpath(response.json(),expr=jsonpathvalue)
        logger1.applog_pen("999999999999999999999999999999999999999999999999999,%s"%assert_vlues[0])
        logger1.applog_pen(exceptvalue)
        # eval(exceptvalue)
        logger1.applog_pen(type(exceptvalue))

        logger1.applog_pen(type(assert_vlues[0]))
        assert str(assert_vlues[0]) == exceptvalue
        logger1.applog_pen("///////////////////////////////////////////////////////////////////////////////////////////////////////")

if __name__ == '__main__':
    pytest.main(['-s',"test_start1.py",'--alluredir', './report/xml'])


#pytest.main(["-s","test_start1.py",'--alluredir', r'C:\Users\10466\Desktop\新建文件夹\pytest_file\test_obiect'])







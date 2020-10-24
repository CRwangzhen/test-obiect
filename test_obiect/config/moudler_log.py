#coding=utf-8
import logging.config
import logging

class logger1():
    def __init__(self):
        logging.config.fileConfig(r"C:\Users\10466\Desktop\新建文件夹\pytest_file\test_obiect\config\logging.comfig", encoding="utf-8")
        self.rootlooger = logging.getLogger('root')
        self.applog = logging.getLogger('applog')

    def root_pen(self,root_vlues):
        self.rootlooger.debug(root_vlues)

    def applog_pen(self,pen_vlues ):
        self.applog.debug(pen_vlues)
logginger = logger1()
# logginger.applog_pen("ddddssdfsddfddrfsd111111111111111")
#从这里引用是这个目录，要用绝对路径


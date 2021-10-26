import unittest,HTMLTestRunner,datetime
from utils.init_folder import init_folder


suit = unittest.defaultTestLoader.discover('./../case_manager/position/',pattern='test_position_modelDowload.py')


if __name__=='__main__':

    date_time = datetime.datetime.now()
    date=date_time.strftime('%Y-%m-%d')
    report_time=date_time.strftime('%H-%M-%S')
    init_folder(date)
    runner=HTMLTestRunner.HTMLTestRunner(open('./../report/html/'+date+'/'+report_time+' test_position_modelDowload.html','wb'),
                                         title='模版下载_html',description='text')
    runner.run(suit)
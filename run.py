import os
import pytest

BASEPATH = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    #要执行的测试用例
    case_path = 'TestCases'
    xml_report_path = 'html'
    args = ['-s', '-q', case_path, '--html=html/nice.html']
    # args = ['-s', '-q', case_path, '--alluredir=./html/report']
    pytest.main(args=args)

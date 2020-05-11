import pytest
from selenium.webdriver.common.by import By
from TestDatas import login_datas as LD

@pytest.mark.usefixtures("access_web")   #函数名称来接受返回值
@pytest.mark.usefixtures("refresh_page")
class TestLogin():

    # #参数化   名字  参数的值
    # @pytest.mark.parametrize('data',LD.phone_data)
    # #异常用例手机号格式不正确(大于11位 小于11位 为空  不在这个号码段)
    # def test_login_0_user_wrongForamt(self,data,access_web):
    #     access_web[1].login(data['user'],data['passwd'])
    #     assert access_web[1].get_errorMsg_from_loginArea()==data['check']


     #正常登录  标记
    @pytest.mark.smoke
    def test_login_1_success(self,access_web):
        access_web[1].login('18684720553',' python')
        assert access_web[1].iselement((By.XPATH,'//a[@href="/Index/logout.html"]'))


if __name__ == '__main__':
    pytest.main(["-q","test_login.py"])





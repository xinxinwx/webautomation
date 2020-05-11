import pytest
from TestDatas import login_datas as LD

@pytest.mark.usefixtures("access_web")   #函数名称来接受返回值
@pytest.mark.usefixtures("refresh_page")
class TestLoginError:

    # 参数化   名字  参数的值
    @pytest.mark.parametrize('data', LD.phone_data)
    # 异常用例手机号格式不正确(大于11位 小于11位 为空  不在这个号码段)
    def test_login_0_user_wrongForamt(self, data, access_web):
        access_web[1].login(data['user'], data['passwd'])
        assert access_web[1].get_errorMsg_from_loginArea() == data['check']
if __name__ == '__main__':
    pytest.main(["-q", "test_login_error.py"])


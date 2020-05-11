from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.loginpage_locators import LoginpageLocator as loc
from Common.basepage import BasePage

class LoginPage(BasePage):

     #登录
     def login(self,username,pwd):
         doc="登录页面_登录功能"
         self.input_text(loc.name_text,username,doc)
         self.input_text(loc.pwd_text,pwd,doc)
         self.click_element(loc.login_bt,doc)


     #获取错误提示信息----登录区域
     def get_errorMsg_from_loginArea(self):
         doc = "登录页面_登录功能"
         return self.get_text(loc.errormsg,doc)


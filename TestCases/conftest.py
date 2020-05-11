import pytest
from selenium import webdriver
from TestDatas import Common_Datas as CD
from PageObejects.login_page import LoginPage

driver=None

#声明它是一个fixture
@pytest.fixture(scope="class")
def access_web():
    global driver
    #前置操作
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(CD.web_login_url)
    loginpage = LoginPage(driver)
    #后置操作
    yield (driver,loginpage)   #分割线 返回值
    driver.quit()


@pytest.fixture
def refresh_page():
    global driver
    #前置操作
    yield
    #后置操作
    driver.refresh()

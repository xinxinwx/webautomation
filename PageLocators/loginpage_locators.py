from selenium.webdriver.common.by import By


class LoginpageLocator:
    # 用户名输入框
    name_text = (By.XPATH, '// input[ @ name = "phone"]')
    # 密码输入框
    pwd_text = (By.XPATH, '// input[ @ name = "password"]')
    # 登录按钮
    login_bt = (By.XPATH, '//button[text()="登录"]')
    # 错误信息提示
    errormsg = (By.XPATH, '//div[@class="form-error-info"] ')
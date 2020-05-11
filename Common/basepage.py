
import logging
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import _datetime
from Common.get_log import GetLogger
from Common.screenshots import take_screenShots
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

#封装基本参数  执行日志   异常处理  失败截图
#所有页面的公共部分


# 获取日志入口
log = GetLogger().getlog()
class BasePage:

    def __init__(self,driver):
        self.driver=driver

    #等待元素可见
    def wait_eleVisible(self,locator,doc="",times=30,poll_frequency=0.5):
         log.info("{0}等待元素{1}可见".format(doc,locator))
         try:
             #开始时间
             start=_datetime.datetime.now()
             WebDriverWait(self.driver,times,poll_frequency).until(EC.visibility_of_element_located(locator))
             #结束时间
             end=_datetime.datetime.now()
             k = end - start
             log.info("{0}{1}元素已可见,等待时长为{2}".format(doc,locator,k.seconds))
         except:
             log.exception("{0}等待{1}元素可见失败!!!!".format(doc,locator))
             take_screenShots(self.driver,doc)
             raise

    #等待元素存在
    def wait_elePresence(self):
        pass

    #查找元素
    def get_element(self,locator,doc=""):
        self.wait_eleVisible(locator,doc);
        log.info("{0}查找元素{1}".format(doc,locator))
        try:
            return  self.driver.find_element(*locator)
        except:
            log.exception("{0}查找{1}元素失败!!!!".format(doc,locator))
            #截图
            take_screenShots(self.driver, doc)


    #点击操作
    def click_element(self,locator,doc=""):
        ele=self.get_element(locator,doc)
        log.info("{0}点击元素{1}".format(doc,locator))
        try:
            ele.click()
        except:
            log.exception("{0}点击{1}操作失败!!!!".format(doc,locator))
            # 截图
            take_screenShots(self.driver, doc)
            raise

    #输入操作
    def input_text(self,locator,text,doc=""):
        ele = self.get_element(locator, doc)
        try:
            log.info("{0}{1}元素输入的值为{2}".format(doc,locator,text))
            ele.send_keys(text)
        except :
            log.exception("{0}输入{1}操作失败!!!!".format(locator,text))
            # 截图
            take_screenShots(self.driver,doc)


    #获取元素的文本内容
    def get_text(self,locator,doc=""):
        ele = self.get_element(locator, doc)
        try:
           log.exception("{0}获取{1}元素的文本内容是{2}".format(doc,locator,ele.text))
           return ele.text
        except:
            log.exception("{0}获取{1}元素的文本内容操作失败!!!!".format(doc,locator))
            # 截图
            take_screenShots(self.driver, doc)
            raise

    #获取元素的属性
    def get_elment_attribute(self,locator,attr,doc=""):
        ele = self.get_element(locator, doc)
        try:
           return  ele.get_attribute(attr)
        except:
            log.exception("{0}获取{1}元素的属性内容操作失败!!!!".format(doc,locator))
            # 截图
            take_screenShots(self.driver, doc)
            raise


    #截图操作
    def save_screenshot(self,name):
        #图片名称:  模块名_页面名称-操作名称_时间.png
        data = _datetime.datetime.now()
        file_name='截屏存放的路径'+"{0}_{1}.png".format(name,data)
        self.driver.save_screenshot(file_name)
        logging.info("截取网页成功。文件路径为{}".format(file_name))
        pass

    """封装鼠标悬停事件"""
    def move_to_element(self, locator):
        el = self.get_element(locator)
        ActionChains(self.driver).move_to_element(el).perform()

    # 判断元素是否存在 存在返回：true
    def iselement(self, loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            log.info("页面中找到{0}元素".format(loc))
            return True
        except:
            log.info("页面中未能找到{0}元素".format(loc))
            return False

    # 切换iframe表单方法
    def base_switch_to_frame(self, frame):
        # 根据frame的id 、name、frame元素
        self.driver.switch_to.frame(frame)


    """js操作浏览器滚动条"""
    def js_scroll_end(self):
        # 滚动到页面底部
        js_height = "window.scrollTo(0, document.body.scrollHeight)"
        self.driver.execute_script(js_height)

    def js_focus(self, locator):
        # 聚焦元素  滚动到元素指定位置
        target = self.get_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        # 回到顶部
        js = 'window.scrollTo(0,0)'
        self.driver.execute_script(js)



    def select_by_index(self, locator, index):
        """通过索引选择下拉框内容"""
        element = self.get_element(locator)
        Select(element).select_by_index(index)

    def click_alert(self):
        '''操作点击弹窗'''
        alert = self.driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)

    def alert_text(self):
        '''返回弹窗的文本内容'''
        alert = self.driver.switch_to.alert()
        rel = alert.text()
        return rel


    def select_by_value(self, locator, value):
        """通过属性值选择下拉框内容"""
        element = self.get_element(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        """通过文本选择下拉框内容"""
        element = self.get_element(locator)
        Select(element).select_by_visible_text(text)

    def click_radio(self, locator):
        """点击单选框或只选择一个复选框"""
        if self.get_element(locator) == False:
            self.click_element(locator)

    def click_checkbox(self, locator):
        """点击复选框(全选)"""
        box_element = self.get_element(locator)
        for box in box_element:
            if box.is_selected() == False:
                box.click()

        # 判断是否被选中
    def isSelected(self, locator):
        element = self.get_element(locator)
        sele = element.is_selected()
        return sele

        # 获取表格行数tr的长度，用于定位table中最后一行的下标
    def lasttable(self, locator):
        tbody = self.get_element(locator)
        tr = tbody.find_elements_by_tag_name("tr")
        return str(len(tr))  # 转换为字符串

        # 分页中，获取最后一页的下标
    def lastpages(self, locator):
        # 通过获取ul下li的长度，获取最后一页的下标
        ul = self.get_element(locator)
        li = ul.find_elements_by_tag_name("li")
        return str(len(li) - 1)







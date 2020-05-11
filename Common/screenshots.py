import os,time,sys
sys.path.append("..\guiTest")
from selenium import webdriver
from Common.get_log import GetLogger

log=GetLogger().logger

def take_screenShots(driver,pic_name):
    now = time.strftime("%Y-%m-%d_%H-%M-%S_")
    log_path = '../screenshots/'
    if not os.path.exists(log_path):  # 如果路径不存在
        os.makedirs(log_path)
    pic=log_path+pic_name+now+".png"
    try:
        driver.get_screenshot_as_file(pic)
        log.error("截图成功，路径为：{}".format(pic))
    except Exception as e:
        log.error("截图失败，原因：{}".format(e))

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://world.taobao.com/")
    take_screenShots(driver,"猜测")
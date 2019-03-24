from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os



def screenshot(driver, file_path=None):
    # 用户并没有传file_path这个参数
    if file_path == None:
        project_path = os.path.dirname(os.getcwd())
        print(project_path)
        file_path = project_path + "/images/"
        # 如果images路径不存在，那么我给创建一个
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        image_name = time.strftime("%Y%m%d-%H%M%S", time.localtime())
        file_path = file_path + image_name + ".png"
        print(file_path)
    driver.save_screenshot(file_path)

try:
    # chromedriver的存储路径
    path = "/Users/zjy/Documents/imooc/code/python_ui/chromedriver"
    driver = webdriver.Chrome(path)
    # 将浏览器最大化
    driver.maximize_window()
    # 打开京东首页
    driver.get("https://www.jd.com/")
    elem = driver.find_element_by_link_text("手机")
    # 鼠标悬停
    ActionChains(driver).move_to_element(elem).perform()
    time.sleep(3)
    old_phone = driver.find_element_by_link_text("老人机")
    old_phone.click()
    # driver.save_screenshot("laorenji.png")
    #浏览器句柄切换
    handles = driver.window_handles
    current_handle = driver.current_window_handle
    for handle in handles:
        if handle != current_handle:
            driver.switch_to.window(handle)
            screenshot(driver)

finally:
    time.sleep(3)
    driver.quit()




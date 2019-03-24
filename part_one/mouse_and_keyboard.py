from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

try:
    # chromedriver的存储路径
    path = "/Users/zjy/Documents/imooc/code/python_ui/chromedriver"
    driver = webdriver.Chrome(path)
    # 将浏览器最大化
    driver.maximize_window()
    # 打开京东首页
    driver.get("https://www.jd.com/")
    # elem = driver.find_element_by_link_text("手机")
    # # 鼠标悬停
    # ActionChains(driver).move_to_element(elem).perform()
    # time.sleep(3)
    # old_phone = driver.find_element_by_link_text("老人机")
    # old_phone.click()

    search_element = driver.find_element_by_id("key")
    search_element.send_keys("电脑")
    search_element.send_keys(Keys.RETURN)


finally:
    time.sleep(3)
    driver.quit()




from selenium import webdriver
import time

path = "/Users/zjy/Documents/imooc/code/python_ui/chromedriver"
driver = webdriver.Chrome(path)
driver.maximize_window()
driver.get("https://www.12306.cn/index/")
from_element = driver.find_element_by_id("fromStationText")
time.sleep(2)
from_element.click()
time.sleep(2)
from_element.send_keys("北京")
time.sleep(2)
driver.find_element_by_xpath("//*[text()='北京北']").click()

to_element = driver.find_element_by_id("toStationText")
to_element.click()
time.sleep(2)
to_element.send_keys("长春")
driver.find_element_by_xpath("//*[text()='长春南']").click()


# 去掉readonly属性
js = "$('input[id=train_date]').removeAttr('readonly')"
driver.execute_script(js)
date_element = driver.find_element_by_id("train_date")
date_element.click()
time.sleep(2)
date_element.clear()
date_element.send_keys("2019-03-10")
time.sleep(2)
driver.find_element_by_class_name("form-label").click()
# 直接点击查询按钮
driver.find_element_by_id("search_one").click()

# 面试题： 在driver操作中，quit和close方法有什么区别
# quit是退出浏览器进程  close是关闭浏览器标签


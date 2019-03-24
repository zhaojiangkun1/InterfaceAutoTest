from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/zjy/Documents/imooc/code/python_ui/chromedriver")
driver.get("https://passport.jd.com/new/login.aspx")

# 强制等待
# time.sleep(3)
# 隐性等待
#driver.implicitly_wait(10)
# 隐性等待就是设置了一个最长的等待，假设在规定的时间内网页加载完成
# 则执行下一步。 否则就一直等到时间截止，然后执行下一步。
# 隐性等待只要设置一次，就围绕着driver的生命周期全都起作用


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#定位元素
locator = (By.CSS_SELECTOR, ".login-tab.login-tab-r")

# 判断账号登陆这个元素是否存在
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator))
element.click()






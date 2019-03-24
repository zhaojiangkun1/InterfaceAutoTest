from selenium import webdriver
import time
import os
import json

path = "/Users/zjy/Documents/imooc/code/python_ui/chromedriver"
driver = webdriver.Chrome(path)
driver.maximize_window()

# 保存cookies到文件中
def save_cookies(driver):
    project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "/cookies/"
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    # 从driver当中获取到cookies
    cookies = driver.get_cookies()

    with open(file_path + "jd.cookies","w") as c:
        # 这里必须用json.dump方法写入文件
        # 将来我们在取cookies的时候会使用json.loads方法，
        # 这里的格式就不匹配了
        json.dump(cookies, c)
    print(cookies)


def login():
    try:
        driver.get("https://www.jd.com")
        driver.find_element_by_class_name("link-login").click()
        driver.find_element_by_link_text("账户登录").click()
        driver.find_element_by_id("loginname").send_keys("16601258428")
        driver.find_element_by_id("nloginpwd").send_keys("123456qwert")
        driver.find_element_by_id("loginsubmit").click()

        # 保存cookies信息到文件中
        save_cookies(driver)
    finally:
        time.sleep(3)

def get_url_with_cookies():

    # 使用https://order.jd.com/center/list.action
# 个人订单页面是否能够访问成功来验证我们的cookies是否有效

    # 获取cookies文件
    project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "/cookies/"
    cookies_file = file_path + "jd.cookies"

    jd_cookies_file = open(cookies_file, "r")
    jd_cookies_str = jd_cookies_file.readline()
    # 加载cookies信息
    jd_cookies_dict = json.loads(jd_cookies_str)

    # 这个地方必须先访问一下网站，然后把旧的cookies删除掉之后
    # 再把我们保存的cookies添加进去
    time.sleep(2)
    driver.get("https://www.jd.com")
    driver.delete_all_cookies()

    # 将cookies信息添加到driver中
    for cookie in jd_cookies_dict:
        driver.add_cookie(cookie)

    time.sleep(2)
    # 检查登陆是否成功
    driver.get("https://order.jd.com/center/list.action")

if __name__ == "__main__":
    # login()
    get_url_with_cookies()


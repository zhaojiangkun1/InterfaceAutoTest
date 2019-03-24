import json
import os


# 把cookies保存到文件中
def save_cookies_to_file(driver):
    # 获取存储cookies的文件夹
    file_path = get_cookies_dir()
    # 获取cookies
    cookies = driver.get_cookies()
    # 存储cookies到文件中
    with open(file_path + "jd.cookies", "w") as f:
        json.dump(cookies, f)

def get_cookies_dir():
    project_path = os.path.dirname(os.getcwd())
    file_path = project_path + "/cookies/"
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    return file_path

def check_cookies(driver):
    # 设置一个登录状态，初始值是未登录
    login_status = False
    # 将cookies信息保存到driver中
    driver = save_cookies_to_driver(driver)

    # 进行跳转链接的检测
    driver.get("https://order.jd.com/center/list.action")
    current_url = driver.current_url
    if current_url == "https://order.jd.com/center/list.action":
        login_status = True
        return login_status
    else:
        return login_status

# 保存cookies信息到driver中
def save_cookies_to_driver(driver):
    cookies_file = get_cookies_file()
    jd_cookies_file = open(cookies_file, "r")
    jd_cookies_str = jd_cookies_file.readline()
    jd_cookies_dict = json.loads(jd_cookies_str)

    # 这里必须清除掉旧的cookies
    driver.get("https://www.jd.com")
    driver.delete_all_cookies()
    for cookie in jd_cookies_dict:
        driver.add_cookie(cookie)
    return driver

def get_cookies_file():
    return get_cookies_dir() + "jd.cookies"


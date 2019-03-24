from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from threading import Thread

# 书写我的业务逻辑
def to_baidu(name, server_address):
    print(name)
    driver = webdriver.Remote(
        command_executor=server_address,
        desired_capabilities=DesiredCapabilities.CHROME
    )
    driver.get("https://www.baidu.com")

my_address = {
    "linux": "http://192.168.1.35:4444/wd/hub",
    "windows": "http://192.168.1.38:4444/wd/hub"
}

threads = []
for name,url in my_address.items():
    t = Thread(target=to_baidu, args=(name, url))
    # t.start()
    threads.append(t)

for t in threads:
    t.start()







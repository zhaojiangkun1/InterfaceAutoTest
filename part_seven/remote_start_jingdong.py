from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from threading import Thread
from part_seven.jingdong import jingdong

def to_jingdong(name, server_address):
    print(name + "启动")
    driver = webdriver.Remote(
        command_executor=server_address,
        desired_capabilities=DesiredCapabilities.CHROME
    )
    driver.maximize_window()
    if name == "linux":
        jingdong.thinkpad_start(driver)
    if name == "windows":
        jingdong.dell_start(driver)

my_address = {
    "linux": "http://192.168.1.35:4444/wd/hub",
    # "windows": "http://192.168.1.38:4444/wd/hub"
}
threads = []
for name, url in my_address.items():
    t = Thread(target=to_jingdong, args=(name, url))
    threads.append(t)

for t in threads:
    t.start()


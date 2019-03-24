from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
try:
    # chromedriver的存储路径
    path = "/Users/zjy/Documents/imooc/code/python_ui/chromedriver"
    driver = webdriver.Chrome(path)
    # 将浏览器最大化
    driver.maximize_window()
    # 打开京东首页
    driver.get("https://www.jd.com/")
    # id定位： 定位搜索框，输入内容后回车，进行搜索
    # search_element = driver.find_element_by_id("key")
    # search_element.send_keys("电脑")
    # # 点击回车进行搜索
    # search_element.send_keys(Keys.RETURN)

    # class_name 定位 ，点击左侧菜单栏中的家用电器
    # menu_item = driver.find_element_by_class_name("cate_menu_lk")
    # menu_item.click()

    # link_text进行左侧菜单栏中的手记链接进行定位
    # link_text = driver.find_element_by_link_text("手机")
    # link_text.click()

    # 使用partial_link_text方法定位，定位汽车用品
    # link_text = driver.find_element_by_partial_link_text("汽车用")
    # link_text.click()
    #
    # x_path = driver.find_element_by_xpath("//*[@id=\"J_cate\"]/ul/li[2]/a[2]")
    # x_path.click()

    css = driver.find_element_by_css_selector("#J_cate > ul > li:nth-child(4) > a:nth-child(7)")
    css.click()

finally:
    time.sleep(3)
    driver.quit()
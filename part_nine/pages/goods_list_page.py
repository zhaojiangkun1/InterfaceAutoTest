from part_nine.pages.base_page import BasePage
from part_nine.config.logging_setting import get_logger
from part_nine.config import basic_config

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class GoodsListPage(BasePage):
    logger = get_logger()

    def __init__(self, driver):
        self._driver = driver
        super(GoodsListPage, self).__init__(driver, basic_config.START_URL)

    def get_goods_list_driver(self, first_list_name, second_list_name):

        """
        获取商品列表的driver
        :param first_list_name: 一级菜单名字
        :param second_list_name: 二级菜单名字
        :return:
        """

        driver = self.open()
        first_element = (By.LINK_TEXT, first_list_name)
        second_element = (By.LINK_TEXT, second_list_name)

        first = self.find_element(*first_element)
        ActionChains(driver).move_to_element(first).perform()
        second = self.find_element(*second_element)
        second.click()

        # 切换句柄
        handles = driver.window_handles
        index_handle = driver.current_window_handle
        for handle in handles:
            if handle != index_handle:
                driver.close()
                driver.switch_to.window(handle)

        self.logger.info("获取到页面" + second_list_name)
        self.logger.info("当前url是:" + driver.current_url)

        self._driver = driver
        return driver


    def get_selector_page(self, selector_condition_list):
        """

        :param selector_condition_list: 筛选条件的list，
                比如 [(By.ID,"id_value"),(By.name,"name_value")]
        :return:
        """
        for condition in selector_condition_list:
            element = self.find_element(*condition)
            element.click()

    def get_goods_info_page(self, selector_condition):
        """
        获取商品的详情页面
        :param selector_condition: 具体商品的筛选条件
                例如: (By.ID,"id_value")
        :return: 浏览器driver
        """
        self.find_element(*selector_condition).click()

        handles = self._driver.window_handles
        index_handle = self._driver.current_window_handle
        for handle in handles:
            if handle != index_handle:
                self._driver.close()
                self._driver.switch_to.window(handle)

        return self._driver





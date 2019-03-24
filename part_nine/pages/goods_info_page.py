from selenium.webdriver.common.by import By

from part_nine.config import basic_config
from part_nine.config.logging_setting import get_logger
from part_nine.model.jingdong_model import Goods
from part_nine.pages.base_page import BasePage


class GoodsInfoPage(BasePage):

    logger = get_logger()

    def __init__(self, driver):
        self._driver = driver
        super(GoodsInfoPage, self).__init__(driver, basic_config.START_URL)
        # self.logger("初始化商品详情页面")

    def save_product_info(self):
        """

        :return:
        """
        js = "window.scrollTo(0,1000)"
        self._driver.execute_script(js)
        # 定位到规格与包装
        product_element = (By.XPATH, "//*[@id=\"detail\"]/div[1]/ul/li[2]")
        self.find_element(*product_element).click()

        info_ele = (By.CLASS_NAME, "Ptable-item")
        info_elements = self.find_elements(*info_ele)

        result_list = []
        for info_element in info_elements:
            info_element_dict = self.__get_info_element_dict(info_element)

            result_list.append(info_element_dict)
            # self.logger.debug(str(info_element_dict))

        self.__save_info_to_mysql(result_list)


    def __save_info_to_mysql(self, info_list):
        goods = Goods()
        for info in info_list:
            for key, value in info.items():
                goods.insert(["computer_part","computer_info"], [str(key), str(value)])

    def __get_info_element_dict(self, info_element):

        # 计算机组成信息，第一列的值
        computer_part_element = (By.TAG_NAME, "h3")
        computer_part = self.find_element(*computer_part_element, element=info_element)

        # 计算机信息中的key值，第二列的值
        computer_info_keys_element = (By.TAG_NAME, "dt")
        computer_info_keys = self.find_elements(*computer_info_keys_element, element=info_element)

        # 计算机信息中的值，就是第三列的值
        computer_info_values_element = (By.XPATH, "dl//dd[not(contains(@class,'Ptable-tips'))]")
        computer_info_values = self.find_elements(*computer_info_values_element, element=info_element)

        self.logger.debug("获取到了所有的规格与包装信息")

        key_and_value_dict = {}
        parts_dict = {}

        for i in range(len(computer_info_keys)):
            key_and_value_dict[computer_info_keys[i].text] = computer_info_values[i].text

        parts_dict[computer_part.text] = key_and_value_dict
        return parts_dict



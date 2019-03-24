from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from part_nine.config import basic_config

class BrowserEngine:

    @staticmethod
    def init_local_driver():
        """
        工具方法，初始化本地的driver，默认是谷歌浏览器
        :return: 返回一个chrome driver
        """
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        driver = webdriver.Chrome(chrome_options=option,
                                  executable_path=basic_config.EXECUTABLE_PATH)

        return driver


    @staticmethod
    def init_local_driver_no_gui():
        """
        工具方法，初始化本地的driver，默认是谷歌浏览器
        :return: 返回一个chrome driver
        """
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=option,
                                  executable_path=basic_config.EXECUTABLE_PATH)

        return driver

    @staticmethod
    def init_remote_driver():
        """
        初始化远程的driver，具体启动哪些取决于在配置文件中的具体配置
        详细配置在basic_config文件中
        :return: result_dict 一个字典，具体的结构是{"名字"：driver}
        """
        remote_browser_dict = basic_config.REMOTE_DRIVER_DICT
        # 用来存储返回结果，结构是{"名字"：driver}
        result_dict = {}

        for name, url in remote_browser_dict.items():
            option = webdriver.ChromeOptions()
            option.add_argument('disable-infobars')
            driver = webdriver.Remote(
                options=option,
                command_executor=url,
                desired_capabilities=DesiredCapabilities.CHROME
            )
            result_dict[name] = driver
        return result_dict



    @staticmethod
    def init_remote_driver_no_gui():
        """
        初始化远程的driver，具体启动哪些取决于在配置文件中的具体配置
        详细配置在basic_config文件中
        :return: result_dict 一个字典，具体的结构是{"名字"：driver}
        """
        remote_browser_dict = basic_config.REMOTE_DRIVER_DICT
        # 用来存储返回结果，结构是{"名字"：driver}
        result_dict = {}

        for name, url in remote_browser_dict.items():
            option = webdriver.ChromeOptions()
            option.add_argument('--headless')
            driver = webdriver.Remote(
                options=option,
                command_executor=url,
                desired_capabilities=DesiredCapabilities.CHROME
            )
            result_dict[name] = driver
        return result_dict

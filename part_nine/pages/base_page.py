from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from part_nine.config import basic_config


class BasePage(object):
    def __init__(self, driver, url):
        """
        BasePage的构造方法
        :param driver: 启动具体哪个浏览器
        :param url: 目标url地址
        """
        self._driver = driver
        self._url = url

    def open(self):
        """
        页面打开方法
        :return: 浏览器的driver
        """
        self._driver.get(url=self._url)
        return self._driver

    def find_element(self,
                     *locator,
                     element=None,
                     timeout=None,
                     wait_type="visibility",
                     when_failed_close_browser=True):
        """
        发现元素方法，分别支持以driver或element之上来进行元素发现的两种定位方式

        :param locator: 元素定位方式，数据类型是元组
                        例如(By.ID,"id_value")
        :param element: 默认值为None，
                如果有值，那么这个值是一个页面元素，这个方法将会在这个元素之上发现它的子元素
        :param timeout: 默认值为None，但是为None时，将会取配置文件中的超时时间配置
        :param wait_type: 等待的类型，支持两种等待方式，一种是可见等待visibility，另外一种是存在等待presence
        :param when_failed_close_browser: 当元素定位失败时，浏览器是否关闭
        :return: 返回定位的元素
        """
        if element is not None:
            return self._init_wait(timeout).until(EC.visibility_of(element.find_element(*locator)))

        try:
            if wait_type == "visibility":
                return self._init_wait(timeout).until(EC.visibility_of_element_located(locator=locator))
            else:
                return self._init_wait(timeout).until(EC.presence_of_element_located(locator=locator))
        except TimeoutException:
            if when_failed_close_browser:
                self._driver.quit()
            raise TimeoutException(msg="定位元素失败,定位方式是:{}".format(locator))
        except NoSuchElementException:
            if when_failed_close_browser:
                self._driver.quit()
            raise NoSuchElementException(msg="定位元素失败,定位方式是:{}".format(locator))


    def find_elements(self,
                     *locator,
                     element=None,
                     timeout=None,
                     wait_type="visibility",
                     when_failed_close_browser=True):

        """
        发现很多元素方法
        :param locator:元素定位方式和值，支持的是元组类型。例如(By.ID,"id_value")
        :param element: 默认值为None，
                如果有值，那么这个值是一个页面元素，这个方法将会在这个元素之上发现它的子元素
        :param timeout: 默认值为None，但是为None时，将会取配置文件中的超时时间配置
        :param wait_type: 等待的类型，支持两种等待方式，一种是可见等待visibility，另外一种是存在等待presence
        :param when_failed_close_browser: 当元素定位失败时，浏览器是否关闭
        :return: 返回定位的元素们
        """

        if element is not None:
            return element.find_elements(*locator)

        try:
            if wait_type == "visibility":
                return self._init_wait(timeout).until(EC.visibility_of_all_elements_located(locator=locator))
            else:
                return self._init_wait(timeout).until(EC.presence_of_all_elements_located(locator=locator))
        except TimeoutException:
            if when_failed_close_browser:
                self._driver.quit()
            raise TimeoutException(msg="定位元素失败,定位方式是:{}".format(locator))
        except NoSuchElementException:
            if when_failed_close_browser:
                self._driver.quit()
            raise NoSuchElementException(msg="定位元素失败,定位方式是:{}".format(locator))



    def _init_wait(self, timeout):
        if timeout is None:
            return WebDriverWait(driver=self._driver, timeout=basic_config.UI_WAIT_TIME)

        else:
            return WebDriverWait(driver=self._driver, timeout=timeout)

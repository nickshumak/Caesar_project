from selenium import webdriver
from front.pages.base_page import BasePage
from front.locators.locators import GroupPageLocators


class GroupsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def my_group(self):
        self.driver.find_element(*GroupPageLocators.MY_GROUP).click()
        return self

    class LeftBar(object):
        """inner classes"""

        def create_group(self):
            return self

        def search_group(self):
            return self

        def edit_group(self):
            return self

        def delete_group(self):
            return self

    class RightBar(object):
        def click_log_out(self):
            pass

    class HeadBar(object):
        pass

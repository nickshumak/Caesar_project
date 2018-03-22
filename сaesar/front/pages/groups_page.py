from front.pages.base_page import BasePage
from front.locators.locators import GroupPageLocators


class GroupsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_button_search(self):
        self.driver.find_element(*GroupPageLocators.BUTTON_SEARCH).click()
        return self

    class LeftBar(object):
        """inner classes"""
        pass

    class RightBar(object):
        pass

    class HeadBar(object):
        pass

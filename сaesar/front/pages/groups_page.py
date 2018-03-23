from front.pages.base_page import BasePage
from front.locators.locators import GroupPageLocators, LeftBarLocators, RightBarLocators


class GroupsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def group_location(self):
        return self.driver.find_element(*GroupPageLocators.GROUP_LOCATION).text

    def button_search(self):
        return self.driver.find_element(*GroupPageLocators.BUTTON_SEARCH)

    def button_my_groups(self):
        return self.driver.find_element(*GroupPageLocators.BUTTON_MY_GROUPS)

    def button_all_groups(self):
        return self.driver.find_element(*GroupPageLocators.BUTTON_ALL_GROUPS)

    def button_ended_groups(self):
        return self.driver.find_element(*GroupPageLocators.ENDED_GROUPS)

    def button_current_groups(self):
        return self.driver.find_element(*GroupPageLocators.CURRENT_GROUPS)

    def button_future_groups(self):
        return self.driver.find_element(*GroupPageLocators.FUTURE_GROUPS)

    def groups_list(self):
        groups_list = []
        groups = self.driver.find_elements(*GroupPageLocators.GROUPS)
        for group in groups:
            groups_list.append(group.text)
        return groups_list
        # return self.driver.find_element(*GroupPageLocators.GROUPS)

    def left_bar(self):
        self.driver.find_element(*GroupPageLocators.LEFT_BAR)
        # return self.LeftBar(self.driver)

    def open_right_bar(self):
        self.driver.find_element(*GroupPageLocators.RIGHT_BAR)

    def get_current_url(self):
        return self.driver.current_url

    class LeftBar(object):
        """inner classes"""

        def __init__(self, driver):
            self.driver = driver

        def create_group(self):
            self.driver.find_element(*LeftBarLocators.BUTTON_CREATE_GROUP)

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

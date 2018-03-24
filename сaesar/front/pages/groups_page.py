from front.pages.base_page import BasePage
from front.pages.login_page import LogInPage
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

    def left_bar(self):
        self.driver.find_element(*GroupPageLocators.LEFT_BAR)
        # return self.LeftBar(self.driver)

    class RightBar(object):
        def __init__(self, driver):
            self.driver = driver

        def click_log_out(self):
            self.driver.find_element(*RightBarLocators.BUTTON_LOGOUT).click()
            return LogInPage(self.driver)

        def user_full_name(self):
            return self.driver.find_element(*RightBarLocators.USER_NAME).text

        def user_role(self):
            return self.driver.find_element(*RightBarLocators.USER_ROLE).text

        def edit_user_button(self):
            self.driver.find_element(*RightBarLocators.BUTTON_EDIT_PROFILE).click()
            return self

    def open_right_bar(self):
        self.driver.find_element(*GroupPageLocators.RIGHT_BAR).click()
        return self.RightBar(self.driver)

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


    class HeadBar(object):
        pass

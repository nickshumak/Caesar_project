from selenium.webdriver.common.action_chains import ActionChains
from caesar_items.pages.base_page import BasePage
from caesar_items.pages.login_page import LogInPage
from caesar_items.locators.locators import \
    GroupPageLocators, LeftMenuLocators, RightMenuLocators, TopMenuLocators


class GroupsPage(BasePage):
    group_page_title = 'Caesar'

    def __init__(self):
        super().__init__()
        self.driver = BasePage.driver

    class LeftMenu(object):
        """inner classes"""

        def __init__(self, driver):
            self.driver = driver

        def create_group(self):
            return self.driver.find_element(*LeftMenuLocators.
                                            BUTTON_CREATE_GROUP)

        def search_group(self):
            return self.driver.find_element(*LeftMenuLocators.
                                            BUTTON_SEARCH_GROUP)

        def edit_group(self):
            return self.driver.find_element(*LeftMenuLocators.
                                            BUTTON_EDIT_GROUP)

        def delete_group(self):
            return self.driver.find_element(*LeftMenuLocators.
                                            BUTTON_DELETE_GROUP)

    class RightMenu(object):
        def __init__(self, driver):
            self.driver = driver

        def log_out_click(self):
            self.driver.find_element(*RightMenuLocators.
                                     BUTTON_LOGOUT).click()
            self.driver.implicitly_wait(2)
            return LogInPage()

        def user_full_name(self):
            return self.driver.find_element(*RightMenuLocators.
                                            USER_NAME).text

        def user_role(self):
            return self.driver.find_element(*RightMenuLocators.
                                            USER_ROLE).text

        def button_user_edit(self):
            self.driver.find_element(*RightMenuLocators.
                                     BUTTON_EDIT_PROFILE).click()

    class TopMenu(object):
        def __init__(self, driver):
            self.driver = driver

        def locations(self):
            self.driver.find_element(*TopMenuLocators.
                                     BUTTON_LOCATIONS).click()
            self.driver.implicitly_wait(2)

        def groups(self):
            self.driver.find_element(*TopMenuLocators.
                                     BUTTON_GROUPS).click()
            self.driver.implicitly_wait(2)
            return GroupsPage()

        def students(self):
            self.driver.find_element(*TopMenuLocators.
                                     BUTTON_STUDENTS).click()
            self.driver.implicitly_wait(2)

        def schedule(self):
            self.driver.find_element(*TopMenuLocators.
                                     BUTTON_SCHEDULE).click()
            self.driver.implicitly_wait(2)

        def add(self):
            self.driver.find_element(*TopMenuLocators.
                                     BUTTON_ADD).click()
            self.driver.implicitly_wait(2)

        def about(self):
            self.driver.find_element(*TopMenuLocators.
                                     BUTTON_ABOUT).click()
            self.driver.implicitly_wait(2)

        def log_out_click(self):
            self.driver.find_element(*TopMenuLocators.
                                     BUTTON_LOGOUT).click()
            self.driver.implicitly_wait(2)

    def group_location(self):
        return self.driver.find_element(*GroupPageLocators.
                                        GROUP_LOCATION).text

    def button_my_groups(self):
        return self.driver.find_element(*GroupPageLocators.
                                        BUTTON_MY_GROUPS)

    def button_all_groups(self):
        return self.driver.find_element(*GroupPageLocators.
                                        BUTTON_ALL_GROUPS)

    def button_ended_groups(self):
        return self.driver.find_element(*GroupPageLocators.
                                        ENDED_GROUPS)

    def button_current_groups(self):
        return self.driver.find_element(*GroupPageLocators.
                                        CURRENT_GROUPS)

    def button_future_groups(self):
        return self.driver.find_element(*GroupPageLocators.
                                        FUTURE_GROUPS)

    def select_group(self, group_title):
        groups = self.driver.find_elements(*GroupPageLocators.
                                           GROUPS)
        for group in groups:
            if group_title == group.text:
                return group.click()

    def left_menu_open(self):
        left_menu = self.driver.find_element(*GroupPageLocators.
                                             LEFT_MENU)
        ActionChains(self.driver).\
            move_to_element_with_offset(left_menu, 105, 300).perform()
        self.driver.implicitly_wait(3)
        return self.LeftMenu(self.driver)

    def right_menu_open(self):
        self.driver.find_element(*GroupPageLocators.USER_PHOTO).click()
        self.driver.implicitly_wait(2)
        return self.RightMenu(self.driver)

    def top_menu_open(self):
        top_menu = self.driver.find_element(*GroupPageLocators.TOP_MENU)
        ActionChains(self.driver).move_to_element(top_menu).perform()
        self.driver.implicitly_wait(2)
        return self.TopMenu(self.driver)

    def get_current_url(self):
        return self.driver.current_url

    def confirm_deletion(self):
        self.driver.find_element(*GroupPageLocators.
                                 BUTTON_CONFIRM_DELETION).click()

    def cancel_deletion(self):
        self.driver.find_element(*GroupPageLocators.
                                 BUTTON_CANCEL_DELETION).click()

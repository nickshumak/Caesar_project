from selenium.webdriver.common.action_chains import ActionChains
from caesar_items.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from caesar_items.locators.locators import \
    GroupPageLocators, LeftMenuLocators, RightMenuLocators, TopMenuLocators


class LeftMenu(object):
    """inner classes"""

    def __init__(self, driver):
        self.driver = driver

    def create_group(self):
        return self.driver.find_element(*LeftMenuLocators.BUTTON_CREATE_GROUP)

    def search_group(self):
        return self.driver.find_element(*LeftMenuLocators.BUTTON_SEARCH_GROUP)

    def edit_group(self):
        return self.driver.find_element(*LeftMenuLocators.BUTTON_EDIT_GROUP)

    def delete_group(self):
        return self.driver.find_element(*LeftMenuLocators.BUTTON_DELETE_GROUP)


class RightMenu(object):
    def __init__(self, driver):
        self.driver = driver

    def log_out_click(self):
        self.driver.find_element(*RightMenuLocators.BUTTON_LOGOUT).click()
        self.driver.implicitly_wait(2)

    def user_full_name(self):
        return self.driver.find_element(*RightMenuLocators.USER_NAME).text

    def user_role(self):
        return self.driver.find_element(*RightMenuLocators.USER_ROLE).text

    def button_user_edit(self):
        self.driver.find_element(*RightMenuLocators.BUTTON_EDIT_PROFILE).click()


class TopMenu(object):
    def __init__(self, driver):
        self.driver = driver

    def locations(self):
        self.driver.find_element(*TopMenuLocators.BUTTON_LOCATIONS).click()
        self.driver.implicitly_wait(2)

    def groups(self):
        self.driver.find_element(*TopMenuLocators.BUTTON_GROUPS).click()
        self.driver.implicitly_wait(2)
        return GroupsPage(self.driver)

    def students(self):
        self.driver.find_element(*TopMenuLocators.BUTTON_STUDENTS).click()
        self.driver.implicitly_wait(2)

    # def click_button_students(self):
    #     actions = ActionChains(self.driver)
    #     actions.move_by_offset('256', '20')
    #     students = WebDriverWait(self.driver, 30).\
    #         until(lambda driver: self.driver.find_element(*TopMenuLocators.
    #                                                       BUTTON_STUDENTS))
    #     actions.click(students)
    #     actions.perform()
    #     return self

    def schedule(self):
        self.driver.find_element(*TopMenuLocators.BUTTON_SCHEDULE).click()
        self.driver.implicitly_wait(2)

    def add(self):
        self.driver.find_element(*TopMenuLocators.BUTTON_ADD).click()
        self.driver.implicitly_wait(2)

    def about(self):
        self.driver.find_element(*TopMenuLocators.BUTTON_ABOUT).click()
        self.driver.implicitly_wait(2)

    def log_out_click(self):
        self.driver.find_element(*TopMenuLocators.BUTTON_LOGOUT).click()
        self.driver.implicitly_wait(2)


class GroupsPage(BasePage):
    group_page_title = 'Caesar'

    def __init__(self, driver):
        super().__init__(driver)
        self.left_menu = LeftMenu(self.driver)
        self.right_menu = RightMenu(self.driver)
        self.top_menu = TopMenu(self.driver)

    def group_location(self):
        return self.driver.find_element(*GroupPageLocators.GROUP_LOCATION).text

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

    def select_group(self, group_title):
        groups = self.driver.find_elements(*GroupPageLocators.GROUPS)
        for group in groups:
            if group_title == group.text:
                return group.click()

    def select_group_students(self, group_name):
        groups_list = WebDriverWait(self.driver, 40).until(
                lambda driver: self.driver.find_elements(*GroupPageLocators.
                                                         GROUPS))
        for group in groups_list:
            if group.text == group_name:
                group.click()
                return self
            elif group.text != group_name:
                print('There is no group with name "{}"'.format(group_name))

    def open_left_menu(self):
        left_menu = self.driver.find_element(*GroupPageLocators.LEFT_MENU)
        ActionChains(self.driver). \
            move_to_element_with_offset(left_menu, 105, 300).perform()
        self.driver.implicitly_wait(3)
        return self.left_menu

    def open_right_menu(self):
        self.driver.find_element(*GroupPageLocators.USER_PHOTO).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(RightMenuLocators.BUTTON_LOGOUT))
        return self.right_menu

    def open_top_menu(self):
        top_menu = self.driver.find_element(*GroupPageLocators.TOP_MENU)
        ActionChains(self.driver).move_to_element(top_menu).perform()
        self.driver.implicitly_wait(3)
        return self.top_menu

    def get_current_url(self):
        return self.driver.current_url

    def confirm_deletion(self):
        self.driver.find_element(*GroupPageLocators.BUTTON_CONFIRM_DELETION).click()

    def cancel_deletion(self):
        self.driver.find_element(*GroupPageLocators.BUTTON_CANCEL_DELETION).click()
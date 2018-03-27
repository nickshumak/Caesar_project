import random

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from front.pages.base_page import BasePage
from front.pages.login_page import LogInPage
from front.caesar_items.locators import GroupPageLocators, LeftMenuLocators, RightMenuLocators, TopMenuLocators, \
    WindowCreateGroup
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support import expected_conditions as EC


class GroupsPage(BasePage):
    driver = None

    def __init__(self, driver):
        super().__init__(driver)
        GroupsPage.driver = driver

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
            time.sleep(1)
            return LogInPage(self.driver)

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
            time.sleep(1)
            # return LocationsPanel(self.driver)

        def groups(self):
            self.driver.find_element(*TopMenuLocators.BUTTON_GROUPS).click()
            time.sleep(1)
            return GroupsPage(self.driver)

        def students(self):
            self.driver.find_element(*TopMenuLocators.BUTTON_STUDENTS).click()
            time.sleep(1)
            # return StudentsPage(self.driver)

        def schedule(self):
            self.driver.find_element(*TopMenuLocators.BUTTON_SCHEDULE).click()
            time.sleep(1)
            # return SchedulePage(self.driver)

        def add(self):
            self.driver.find_element(*TopMenuLocators.BUTTON_ADD).click()
            time.sleep(1)
            # return AddPage(self.driver)

        def about(self):
            self.driver.find_element(*TopMenuLocators.BUTTON_ABOUT).click()
            time.sleep(1)
            # return AboutPage(self.driver)

        def log_out_click(self):
            self.driver.find_element(*TopMenuLocators.BUTTON_LOGOUT).click()
            time.sleep(1)

    class WindowCreatingGroup(object):
        def __init__(self):
            self.driver = GroupsPage.driver

        def group_name_setting(self, new_name):
            self.driver.find_element(*WindowCreateGroup.FIELD_GROUP_NAME).send_keys(new_name)
            return self

        def name_of_group_save_to_variable(self) -> str:
            name_of_group = self.driver.find_element(*WindowCreateGroup.FIELD_GROUP_NAME).get_attribute("value")
            while len(name_of_group) > 20:
                if len(name_of_group) > 20:
                    self.driver.find_element(*WindowCreateGroup.FIELD_GROUP_NAME).send_keys(Keys.BACKSPACE)
                    name_of_group = self.driver.find_element(*WindowCreateGroup.FIELD_GROUP_NAME).get_attribute("value")
                else:
                    break
            return name_of_group

        def direction_of_group_choosing(self, index) -> object:
            self.driver.find_element(*WindowCreateGroup.SPINNER_DIRECTION).click()
            select = Select(self.driver.find_element(*WindowCreateGroup.SPINNER_DIRECTION))
            select.select_by_index(index)
            return self

        def direction_of_group_save_to_variable(self) -> str:
            # direction = self.driver.find_element(
            #     *WindowCreateGroup.SPINNER_DIRECTION)
            direction_of_group = self.driver.find_element(*WindowCreateGroup.SPINNER_DIRECTION).get_attribute("value")
            return direction_of_group

        def location_of_group_choosing(self) -> object:
            self.driver.find_element(*WindowCreateGroup.SPINNER_LOCATION).click()
            options_list = self.driver.find_element(*WindowCreateGroup.SPINNER_LOCATION)
            locations_list = options_list.find_elements(By.TAG_NAME, 'option')
            random_location_index = random.randint(0, len(locations_list) - 1)
            select = Select(self.driver.find_element(*WindowCreateGroup.SPINNER_LOCATION))
            select.select_by_index(random_location_index)
            return self

        def location_of_group_save_to_variable(self) -> str:
            location_of_group = self.driver.find_element(*WindowCreateGroup.SPINNER_LOCATION).get_attribute("value")
            return location_of_group

        def teachers_adding(self, index) -> object:
            self.driver.find_element(*WindowCreateGroup.BUTTON_TEACHERS_ADD).click()
            self.driver.find_element(*WindowCreateGroup.SPINNER_TEACHERS).click()
            select = Select(self.driver.find_element(*WindowCreateGroup.SPINNER_TEACHERS))
            select.select_by_index(index)
            self.driver.find_element(*WindowCreateGroup.BUTTON_ACCEPT_TEACHER).click()
            return self

        def date_start_setting(self, start_date_value):
            date_start_field = self.driver.find_element(*WindowCreateGroup.DATE_START)
            date_start_field.send_keys(start_date_value)
            date_finish_field = self.driver.find_element(*WindowCreateGroup.DATE_FINISH)
            date_finish_field.send_keys(Keys.ENTER)
            return self

        def submit_group_creating(self):
            self.driver.find_element(*WindowCreateGroup.BUTTON_SAVE).click()
            return self

        # def date_start_save_to_variable(self) -> str:
        #     date_start = self.driver.find_element(*WindowCreateGroup.DATE_START)
        #     date_start=date_start.find_element("value placeholder").text()
        #     return date_start

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

    def left_menu_open(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#left-menu > div')))
        left_menu = self.driver.find_element(*GroupPageLocators.LEFT_MENU)
        ActionChains(self.driver).move_to_element_with_offset(left_menu, 100, 200).perform()
        return self.LeftMenu(self.driver)

    def right_menu_open(self):
        self.driver.find_element(*GroupPageLocators.USER_PHOTO).click()
        time.sleep(1)
        return self.RightMenu(self.driver)

    def top_menu_open(self):
        top_menu = self.driver.find_element(*GroupPageLocators.TOP_MENU)
        ActionChains(self.driver).move_to_element(top_menu).perform()
        time.sleep(1)
        return self.TopMenu(self.driver)

    def get_current_url(self):
        return self.driver.current_url

import random

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from caesar_items.pages.base_page import BasePage
from caesar_items.pages.login_page import LogInPage
from caesar_items.locators.locators import GroupPageLocators, LeftMenuLocators, RightMenuLocators, TopMenuLocators, \
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
            button_create_group = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, LeftMenuLocators.BUTTON_CREATE_GROUP_XPATH)))
            return button_create_group

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

        def field_group_name_appeal_to(self) -> object:
            field_name_of_group = self.driver.find_element(
                By.NAME, WindowCreateGroup.FIELD_NAME_GROUPS_NAME)
            return field_name_of_group

        def field_group_name_setting(self, new_group_name) -> object:
            field_name_of_group = self.driver.find_element(
                By.NAME, WindowCreateGroup.FIELD_NAME_GROUPS_NAME)
            field_name_of_group.clear()
            field_name_of_group.send_keys(new_group_name)
            return self

        def name_of_group_save_to_variable(self) -> str:
            field_name_of_group = self.driver.find_element(
                By.NAME, WindowCreateGroup.FIELD_NAME_GROUPS_NAME)
            name_of_group = field_name_of_group.get_attribute(
                "value")
            # while len(name_of_group) > 20:
            #     if len(name_of_group) > 20:
            #         field_name_of_group.send_keys(Keys.BACKSPACE)
            #         name_of_group = field_name_of_group.get_attribute(
            #             "value")
            #     else:
            #         break
            return name_of_group

        def direction_of_group_appeal_to(self) -> object:
            spinner_direction = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((
                    By.NAME, WindowCreateGroup.SPINNER_DIRECTION_NAME)))
            return spinner_direction

        def direction_of_group_select(self, index) -> object:
            spinner_direction = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((
                    By.NAME, WindowCreateGroup.SPINNER_DIRECTION_NAME)))
            select_direction = Select(spinner_direction)
            select_direction.select_by_index(index)
            return self

        def direction_of_group_random_select(self) -> object:
            spinner_direction = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((
                    By.NAME, WindowCreateGroup.SPINNER_DIRECTION_NAME)))
            spinner_direction.click()
            directions_list = spinner_direction.find_elements(By.TAG_NAME, 'option')
            random_direction_index = random.randint(1, len(directions_list) - 1)
            select_direction = Select(spinner_direction)
            select_direction.select_by_index(random_direction_index)
            return self

        def direction_of_group_save_to_variable(self) -> str:
            spinner_direction = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((
                    By.NAME, WindowCreateGroup.SPINNER_DIRECTION_NAME)))
            direction_selected = spinner_direction.get_attribute("value")
            return direction_selected

        def location_of_group_appeal_to(self) -> object:
            spinner_location = self.driver.find_element(
                By.NAME, WindowCreateGroup.SPINNER_LOCATION_NAME)
            return spinner_location

        def location_of_group_random_select(self) -> object:
            spinner_location = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((
                    By.NAME, WindowCreateGroup.SPINNER_LOCATION_NAME)))
            spinner_location.click()
            locations_list = spinner_location.find_elements(By.TAG_NAME, 'option')
            random_location_index = random.randint(0, len(locations_list) - 1)
            select_location = Select(spinner_location)
            select_location.select_by_index(random_location_index)
            return self

        def location_of_group_select_by_index(self, location_index) -> object:
            spinner_location = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((
                    By.NAME, WindowCreateGroup.SPINNER_LOCATION_NAME)))
            spinner_location.click()
            select_location = Select(spinner_location)
            select_location.select_by_index(location_index)
            return self

        def location_of_group_save_to_variable(self) -> str:
            spinner_location_of_group = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((
                    By.NAME, WindowCreateGroup.SPINNER_LOCATION_NAME)))
            location_of_group = spinner_location_of_group.get_attribute("value")
            return location_of_group

        def teachers_adding(self, index) -> object:
            button_add_teacher = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(WindowCreateGroup.BUTTON_TEACHERS_ADD))
            button_add_teacher.click()
            self.driver.find_element(*WindowCreateGroup.SPINNER_TEACHERS).click()
            select = Select(self.driver.find_element(*WindowCreateGroup.SPINNER_TEACHERS))
            select.select_by_index(index)
            self.driver.find_element(*WindowCreateGroup.BUTTON_ACCEPT_TEACHER).click()
            return self

        def date_start_setting(self, start_date_value):
            field_date_start_field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(WindowCreateGroup.DATE_START))
            field_date_start_field.send_keys(start_date_value)
            field_date_finish = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(WindowCreateGroup.DATE_FINISH))
            field_date_finish.send_keys(Keys.ENTER)
            return self

        def submit_group_creating(self):
            button_save_group = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(WindowCreateGroup.BUTTON_SAVE))
            button_save_group.click()
            return self

        # def date_start_save_to_variable(self) -> str:
        #     date_start = self.driver.find_element(*WindowCreateGroup.DATE_START)
        #     date_start=date_start.find_element("value placeholder").text()
        #     return date_start
        def catch_hint(self) -> object:
            # field_name_of_group = self.driver.find_element(
            #     By.NAME, WindowCreateGroup.FIELD_NAME_GROUPS_NAME)
            # field_name_of_group.clear()
            spinner_location = self.driver.find_elements(By.CLASS_NAME, 'hint')
            for spinner in spinner_location:
                sp = spinner.find_elements(By.TAG_NAME, 'p')
                for s in sp:
                    print(s.text)
            # spinner_location = WebDriverWait(self.driver, 4).until(
            #     EC.(By.CSS_SELECTOR, "#modal-window > section > section > section > div:nth-child(1) > div:nth-child(1) > div > div > div:nth-child(4)"))
            # spinner_location.click()
            # select_location = Select(spinner_location)
            # select_location.select_by_index(location_index)
            return self

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

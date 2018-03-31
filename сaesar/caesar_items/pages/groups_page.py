# from caesar_items.pages.login_page import LogInPage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from caesar_items.locators.locators import \
    GroupPageLocators, LeftMenuLocators, RightMenuLocators, TopMenuLocators, WindowCreateGroup
from caesar_items.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


class LeftMenu(object):


    def __init__(self, driver):
        self.driver = driver

    def create_group(self):
        try:
            return WebDriverWait(self.driver, 10) \
                .until(EC.element_to_be_clickable(LeftMenuLocators.BUTTON_CREATE_GROUP))
        except NoSuchElementException:
            raise NoSuchElementException

    def search_group(self):
        return self.driver.find_element(*LeftMenuLocators.BUTTON_SEARCH_GROUP)

    def edit_group(self):
        try:
            return self.driver.find_element(*LeftMenuLocators.BUTTON_EDIT_GROUP)
        except NoSuchElementException:
            raise NoSuchElementException

    def delete_group(self):
        try:
            return self.driver.find_element(*LeftMenuLocators.BUTTON_DELETE_GROUP)
        except NoSuchElementException:
            raise NoSuchElementException


class RightMenu(object):
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        self.driver.implicitly_wait(2)
        self.driver.find_element(*RightMenuLocators.BUTTON_LOGOUT).click()

    def user_full_name(self):
        return self.driver.find_element(*RightMenuLocators.USER_NAME).text

    def user_role(self):
        return self.driver.find_element(*RightMenuLocators.USER_ROLE).text

    def edit_user(self):
        self.driver.find_element(*RightMenuLocators.BUTTON_EDIT_PROFILE).click()


class TopMenu(object):
    def __init__(self, driver):
        self.driver = driver

    def locations(self):
        self.driver.find_element(*TopMenuLocators.BUTTON_LOCATIONS).click()
        self.driver.implicitly_wait(2)
        # return LocationsPanel(self.driver)

    def groups(self):
        self.driver.find_element(*TopMenuLocators.BUTTON_GROUPS).click()
        self.driver.implicitly_wait(2)

    def students(self):
        self.driver.find_element(*TopMenuLocators.BUTTON_STUDENTS).click()
        self.driver.implicitly_wait(2)
        # return StudentsPage(self.driver)

    def schedule(self):
        self.driver.find_element(*TopMenuLocators.BUTTON_SCHEDULE).click()
        self.driver.implicitly_wait(2)
        # return SchedulePage(self.driver)

    def add(self):
        self.driver.find_element(*TopMenuLocators.BUTTON_ADD).click()
        self.driver.implicitly_wait(2)
        # return AddPage(self.driver)

    def about(self):
        self.driver.find_element(*TopMenuLocators.BUTTON_ABOUT).click()
        self.driver.implicitly_wait(2)
        # return AboutPage(self.driver)

    def logout(self):
        self.driver.find_element(*TopMenuLocators.BUTTON_LOGOUT).click()
        self.driver.implicitly_wait(2)


class GroupsPage(BasePage):
    group_page_title = 'Caesar'
    driver = None

    def __init__(self, driver):
        super().__init__(driver)
        GroupsPage.driver = driver
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

    def open_left_menu(self):
        left_menu = self.driver.find_element(*GroupPageLocators.LEFT_MENU)
        ActionChains(self.driver). \
            move_to_element_with_offset(left_menu, 105, 300).perform()
        WebDriverWait(self.driver, 10) \
            .until(EC.visibility_of_element_located(LeftMenuLocators.BUTTON_SEARCH_GROUP))
        return self.left_menu

    def open_right_menu(self):
        self.driver.find_element(*GroupPageLocators.USER_PHOTO).click()
        self.driver.implicitly_wait(3)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(RightMenuLocators.BUTTON_LOGOUT))
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

    class WindowCreatingGroup(object):
        def __init__(self):
            self.driver = GroupsPage.driver

        def field_group_name_get(self) -> object:
            return WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(WindowCreateGroup.
                                           FIELD_GROUP_NAME))

        def field_group_name_set(self, new_group_name) -> object:
            field_name_of_group = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(WindowCreateGroup.
                                           FIELD_GROUP_NAME))
            field_name_of_group.clear()
            field_name_of_group.send_keys(new_group_name)
            return self

        def field_group_name_clear(self) -> object:
            field_name_of_group = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(WindowCreateGroup.
                                           FIELD_GROUP_NAME))
            field_name_of_group.clear()
            return self

        def field_group_name_value_get(self) -> str:
            return WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    WindowCreateGroup.FIELD_GROUP_NAME)). \
                get_attribute("value")

        def direction_of_group_get(self) -> object:
            return WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(WindowCreateGroup.
                                           DROP_LIST_DIRECTION))

        def direction_of_group_select(self, str_direction) -> object:
            list_direction = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(WindowCreateGroup.
                                           DROP_LIST_DIRECTION))
            select_direction = Select(list_direction)
            select_direction.select_by_index(str_direction)
            return self

        def direction_of_group_value_get(self) -> str:
            return WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(
                    WindowCreateGroup.DROP_LIST_DIRECTION)). \
                get_attribute("value")

        def location_of_group_get(self) -> object:
            return WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(WindowCreateGroup.
                                           DROP_LIST_LOCATION))

        def location_of_group_select(self, location_index) -> object:
            locations_get = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(WindowCreateGroup.
                                           DROP_LIST_LOCATION))
            locations_get.click()
            select_location = Select(locations_get)
            select_location.select_by_index(location_index)
            return self

        def location_of_group_save_to_variable(self) -> str:
            spinner_location_of_group = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(WindowCreateGroup.
                                           DROP_LIST_LOCATION))
            location_of_group = spinner_location_of_group. \
                get_attribute("value")
            return location_of_group

        def teachers_adding(self, teacher_name) -> object:
            button_add_teacher = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(WindowCreateGroup.
                                           BUTTON_TEACHERS_ADD))
            button_add_teacher.click()
            drop_list_teachers = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(WindowCreateGroup.
                                           DROP_LIST_TEACHERS))
            drop_list_teachers.click()
            select = Select(drop_list_teachers)
            select.select_by_index(teacher_name)
            self.driver.find_element(*WindowCreateGroup.
                                     BUTTON_ACCEPT_TEACHER).click()
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

        def warning_message_get(self) -> object:
            hints = self.driver.find_elements(By.CLASS_NAME, 'hint')
            for warning_messages in hints:
                warning_message = warning_messages.find_elements(
                    By.TAG_NAME, 'p')
                for message_text in warning_message:
                    print(message_text.text)
            return self

        def warning_message_get(self) -> object:
            warning_message = None
            form = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(WindowCreateGroup.
                                                 FORM_GROUP_NAME))
            hints = form.find_elements(By.CLASS_NAME, 'hint')
            for hint in hints:
                hint = hint.find_elements(
                    By.TAG_NAME, 'p')
                for message_text in hint:
                    warning_message = message_text.text
            return warning_message

        def warning_message_get_by_locator(self, locator) -> object:
            warning_message = None
            form = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(locator))
            hints = form.find_elements(By.CLASS_NAME, 'hint')
            for hint in hints:
                hint = hint.find_elements(
                    By.TAG_NAME, 'p')
                for message_text in hint:
                    warning_message = message_text.text
            return warning_message

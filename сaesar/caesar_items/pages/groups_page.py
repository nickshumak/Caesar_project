import random

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from caesar_items.locators.locators import \
    GroupPageLocators, LeftMenuLocators, RightMenuLocators, TopMenuLocators, \
    CreateGroupWindowLocators
from caesar_items.pages.base_page import BasePage
from caesar_items.pages.admin_page import AdminPage
from resource.url_site import PathUrl
from resource.constants_creating_group import TIME_TO_WAIT, TEST_TEACHER_INDEX, \
    TEST_FIRST_EXPERT_NAME, TEST_START_DATE


class LeftMenu(object):
    def __init__(self, driver):
        self.driver = driver

    def create_group_button(self):
        """
        get create button web element
        """
        return WebDriverWait(self.driver, TIME_TO_WAIT).until(
            EC.visibility_of_element_located(LeftMenuLocators.BUTTON_CREATE_GROUP))

    def search_group_button(self):
        """
        get search button web element
        """
        return self.driver.find_element(*LeftMenuLocators.BUTTON_SEARCH_GROUP)

    def edit_group_button(self):
        """
        get edit button web element
        """
        return self.driver.find_element(*LeftMenuLocators.BUTTON_EDIT_GROUP)

    def delete_group_button(self):
        """
        get delete button web element
        """
        return self.driver.find_element(*LeftMenuLocators.BUTTON_DELETE_GROUP)


class RightMenu(object):
    def __init__(self, driver):
        self.driver = driver

    def click_logout_button(self):
        self.driver.implicitly_wait(2)
        self.driver.find_element(*RightMenuLocators.BUTTON_LOGOUT).click()

    def get_user_full_name_text(self):
        return self.driver.find_element(*RightMenuLocators.USER_NAME).text

    def get_user_role_text(self):
        return self.driver.find_element(*RightMenuLocators.USER_ROLE).text

    def click_edit_user_button(self):
        self.driver.find_element(*RightMenuLocators.BUTTON_EDIT_PROFILE).click()


class TopMenu(object):
    def __init__(self, driver):
        self.driver = driver

    def click_locations_button(self):
        self.driver.find_element(*TopMenuLocators.BUTTON_LOCATIONS).click()
        self.driver.implicitly_wait(2)
        # return LocationsPanel(self.driver)

    def click_groups_button(self):
        self.driver.find_element(*TopMenuLocators.BUTTON_GROUPS).click()
        self.driver.implicitly_wait(2)

    def click_students_button(self):
        self.driver.find_element(*TopMenuLocators.BUTTON_STUDENTS).click()
        self.driver.implicitly_wait(2)
        # return StudentsPage(self.driver)

    def click_schedule_button(self):
        self.driver.find_element(*TopMenuLocators.BUTTON_SCHEDULE).click()
        self.driver.implicitly_wait(2)
        # return SchedulePage(self.driver)

    def click_add_button(self):
        self.driver.find_element(*TopMenuLocators.BUTTON_ADD).click()
        self.driver.implicitly_wait(2)
        # return AddPage(self.driver)

    def click_about_button(self):
        self.driver.find_element(*TopMenuLocators.BUTTON_ABOUT).click()
        self.driver.implicitly_wait(2)
        # return AboutPage(self.driver)

    def click_logout_button(self):
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

    def get_group_location_text(self):
        return self.driver.find_element(*GroupPageLocators.GROUP_LOCATION).text

    def my_group_button(self):
        return self.driver.find_element(*GroupPageLocators.BUTTON_MY_GROUPS)

    def all_groups_button(self):
        return self.driver.find_element(*GroupPageLocators.BUTTON_ALL_GROUPS)

    def ended_groups_button(self):
        return self.driver.find_element(*GroupPageLocators.ENDED_GROUPS)

    def current_groups_button(self):
        return self.driver.find_element(*GroupPageLocators.CURRENT_GROUPS)

    def button_boarding_groups(self):
        return self.driver.find_element(*GroupPageLocators.BOARDING_GROUPS)

    def select_group_by_name(self, group_name):
        groups = self.driver.find_elements(*GroupPageLocators.GROUPS)
        for group in groups:
            if group_name == group.text:
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

    def open_admin_page(self):
        self.driver.get(PathUrl().ADMIN_PAGE)
        return AdminPage(self.driver)

    def get_current_url(self):
        return self.driver.current_url

    def get_group_stage_text(self):
        group_stage = WebDriverWait(self.driver, 10) \
            .until(EC.visibility_of_element_located(GroupPageLocators.GROUP_STAGE))
        return group_stage.text

    def click_confirm_deletion_button(self):
        self.driver.find_element(*GroupPageLocators.BUTTON_CONFIRM_DELETION).click()

    def click_cancel_deletion_button(self):
        self.driver.find_element(*GroupPageLocators.BUTTON_CANCEL_DELETION).click()

    class CreateGroupWindow(object):
        def __init__(self):
            self.driver = GroupsPage.driver

        def get_group_name_field(self) -> object:
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           GROUP_NAME_FIELD))

        def set_group_name(self, new_group_name) -> object:
            field_name_of_group = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           GROUP_NAME_FIELD))
            field_name_of_group.clear()
            field_name_of_group.send_keys(new_group_name)
            return self

        def clear_group_name_field(self) -> object:
            field_name_of_group = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           GROUP_NAME_FIELD))
            field_name_of_group.clear()
            return self

        def get_group_name_form(self):
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.presence_of_element_located(CreateGroupWindowLocators.
                                               GROUP_NAME_FORM))

        def get_group_direction_form(self):
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.presence_of_element_located(CreateGroupWindowLocators.
                                               DIRECTION_FORM))

        def get_group_location_form(self):
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.presence_of_element_located(CreateGroupWindowLocators.
                                               LOCATION_FORM))

        def get_start_date_form(self):
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.presence_of_element_located(CreateGroupWindowLocators.
                                               START_DATE_FORM))

        def get_experts_form(self):
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.presence_of_element_located(CreateGroupWindowLocators.
                                               EXPERTS_FORM))

        def get_value_group_name_field(self) -> str:
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(
                    CreateGroupWindowLocators.GROUP_NAME_FIELD)). \
                get_attribute("value")

        def get_group_direction(self) -> object:
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           DIRECTION_DROP_LIST))

        def set_group_direction(self, str_direction) -> object:
            list_direction = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           DIRECTION_DROP_LIST))
            select_direction = Select(list_direction)
            select_direction.select_by_index(str_direction)
            return self

        def get_value_of_direction(self) -> str:
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(
                    CreateGroupWindowLocators.DIRECTION_DROP_LIST)). \
                get_attribute("value")

        def get_group_location(self) -> object:
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           LOCATION_DROP_LIST))

        def set_group_location(self, location_index) -> object:
            locations_get = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           LOCATION_DROP_LIST))
            locations_get.click()
            select_location = Select(locations_get)
            select_location.select_by_index(location_index)
            return self

        def get_value_of_location(self) -> str:
            spinner_location_of_group = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           LOCATION_DROP_LIST))
            location_of_group = spinner_location_of_group. \
                get_attribute("value")
            return location_of_group

        def get_teacher_add_button(self) -> object:
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           ONE_MORE_TEACHER_BUTTON))

        def get_teachers_drop_list(self) -> object:
            button_add_teacher = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           ONE_MORE_TEACHER_BUTTON))
            button_add_teacher.click()
            drop_list_teachers = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           TEACHERS_DROP_LIST))
            return drop_list_teachers

        def select_teacher(self, teacher_name) -> object:
            button_add_teacher = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           ONE_MORE_TEACHER_BUTTON))
            button_add_teacher.click()
            drop_list_teachers = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           TEACHERS_DROP_LIST))
            drop_list_teachers.click()
            select = Select(drop_list_teachers)
            select.select_by_index(teacher_name)
            self.driver.find_element(CreateGroupWindowLocators.
                                     ACCEPT_TEACHER_BUTTON).click()
            return self

        def add_teacher(self):
            button_add_teacher = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           ONE_MORE_TEACHER_BUTTON))
            button_add_teacher.click()
            WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           ACCEPT_TEACHER_BUTTON)).click()
            return self

        def get_added_teachers_list(self):
            added_teachers_form = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.presence_of_element_located(CreateGroupWindowLocators.
                                               ADDED_TEACHERS_FORM))
            added_teachers_list = added_teachers_form.find_elements(By.CLASS_NAME, 'list-item')
            list_of_teachers_values = []
            for added_teacher in added_teachers_list:
                list_of_teachers_values.append(added_teacher.text)
            return list_of_teachers_values

        def set_start_date(self, start_date_value):
            field_date_start_field = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           START_DATE_FIELD))
            field_date_start_field.send_keys(start_date_value)
            field_date_finish = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           FINISH_DATE_FIELD))
            field_date_finish.send_keys(Keys.ENTER)
            return self

        def submit_group_creating_button(self):
            button_save_group = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           SAVE_BUTTON))
            button_save_group.click()
            return self

        def get_save_group_button(self):
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           SAVE_BUTTON))

        def get_warning_message_by_form(self, form) -> object:
            warning_message = None
            hints = form.find_elements(By.CLASS_NAME, 'hint')
            for hint in hints:
                hint = hint.find_elements(
                    By.TAG_NAME, 'p')
                for message_text in hint:
                    warning_message = message_text.text
            return warning_message

        def cancel_button_get(self):
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           CANCEL_BUTTON))

        def add_expert(self, expert_name):
            WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(
                    CreateGroupWindowLocators.ADD_EXPERT_BUTTON)).click()
            WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(
                    CreateGroupWindowLocators.EXPERTS_NAME_FIELD)). \
                send_keys(expert_name)
            WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(
                    CreateGroupWindowLocators.ACCEPT_EXPERT_BUTTON)).click()
            return self

        def get_added_experts_list(self):
            added_experts_form = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.presence_of_element_located(CreateGroupWindowLocators.
                                               ADDED_EXPERTS_LIST))
            added_experts_list = added_experts_form.find_elements(By.CLASS_NAME, 'list-item')
            list_of_values = []
            for added_expert in added_experts_list:
                list_of_values.append(added_expert.text)
            return list_of_values

        def auto_fill_all_fields(self, new_group_name):
            direction_field = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           DIRECTION_DROP_LIST))
            direction_field.click()
            directions_list = direction_field.find_elements(
                By.TAG_NAME, 'option')
            random_direction_index = random.randint(
                1, len(directions_list) - 1)
            select_direction = Select(direction_field)
            select_direction.select_by_index(random_direction_index)
            location_field = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           LOCATION_DROP_LIST))
            location_field.click()
            random_location_index = random.randint(0, 3)
            select_location = Select(location_field)
            select_location.select_by_index(random_location_index)
            button_add_teacher = WebDriverWait(self.driver, TIME_TO_WAIT). \
                until(EC.element_to_be_clickable(CreateGroupWindowLocators.
                                                 ONE_MORE_TEACHER_BUTTON))
            button_add_teacher.click()
            drop_list_teachers = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           TEACHERS_DROP_LIST))
            drop_list_teachers.click()
            select = Select(drop_list_teachers)
            select.select_by_index(TEST_TEACHER_INDEX)
            WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           ACCEPT_TEACHER_BUTTON)).click()
            WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           ADD_EXPERT_BUTTON)).click()
            WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(
                    CreateGroupWindowLocators.EXPERTS_NAME_FIELD)).send_keys(
                TEST_FIRST_EXPERT_NAME)
            WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           ACCEPT_EXPERT_BUTTON)).click()
            field_date_start_field = WebDriverWait(self.driver,
                                                   TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           START_DATE_FIELD))
            field_date_start_field.send_keys(TEST_START_DATE)
            field_date_finish = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           FINISH_DATE_FIELD))
            field_date_finish.send_keys(Keys.ENTER)
            field_name_of_group = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           GROUP_NAME_FIELD))
            field_name_of_group.clear()
            field_name_of_group.send_keys(new_group_name)
            WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           SAVE_BUTTON)).click()

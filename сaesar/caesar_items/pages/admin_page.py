from selenium.common.exceptions import NoSuchElementException, \
    StaleElementReferenceException
from selenium.webdriver.common.by import By
from caesar_items.locators.locators import AdminPageLocators, \
    CreateEditUsersLocators, CreateEditGroupsLocators, \
    CreateEditStudentsLocators
from caesar_items.pages.base_page import BasePage
from caesar_items.pages.groups_page import GroupsPage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def tab_users(self):
        """go to the users tab"""
        tab_users = self.driver.find_element(*AdminPageLocators.TAB_USERS)
        tab_users.click()
        return self

    def tab_groups(self):
        """go to the groups tab"""
        tab_groups = self.driver.find_element(*AdminPageLocators.TAB_GROUPS)
        tab_groups.click()
        return self

    def tab_students(self):
        """go to the students tab"""
        tab_students = self.driver.find_element(
            *AdminPageLocators.TAB_STUDENTS)
        tab_students.click()
        return self

    def add_entity_user(self):
        """add user in table"""
        add_entity = self.driver.find_element(*AdminPageLocators.ADD_USER)
        add_entity.click()
        return self

    def add_entity_group(self):
        """add group in table"""
        add_entity = self.driver.find_element(*AdminPageLocators.ADD_GROUP)
        add_entity.click()
        return self

    def add_entity_student(self):
        """add student in table"""
        add_entity = self.driver.find_element(*AdminPageLocators.ADD_STUDENT)
        add_entity.click()
        return self

    def back_home(self):
        """click on the button that will return to the Group page"""
        back_home = self.driver.find_element(*AdminPageLocators.BUTTON_ESCAPE)
        back_home.click()
        return GroupsPage(self.driver)

    def fill_user_name(self, name):
        first_name = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "firstName")))
        first_name.click()
        first_name.send_keys(name, Keys.ENTER)
        return self

    def fill_user_second_name(self, second_name):
        last_name = self.driver.find_element(
            *CreateEditUsersLocators.LAST_NAME)
        last_name.click()
        last_name.send_keys(second_name)
        return self

    def fill_user_type_role(self, type_role):
        role = self.driver.find_element(
            *CreateEditUsersLocators.ROLE)
        role.click()
        Select(role).select_by_visible_text(type_role)
        return self

    def fill_user_city(self, city):
        location = self.driver.find_element(
            *CreateEditUsersLocators.LOCATION)
        location.click()
        Select(location).select_by_visible_text(city)
        return self

    def fill_user_photo(self, photo):
        photograph = self.driver.find_element(*CreateEditUsersLocators.PHOTO)
        photograph.click()
        photograph.send_keys(photo)
        return self

    def fill_user_login(self, log_in):
        login = self.driver.find_element(
            *CreateEditUsersLocators.LOGIN_FIELD)
        login.click()
        login.send_keys(log_in)
        return self

    def fill_user_password(self, secret):
        password = self.driver.find_element(
            *CreateEditUsersLocators.PASSWORD_FIELD)
        password.click()
        password.send_keys(secret)
        return self

    def get_condition_button(self):
        return self.driver.find_element(
            *AdminPageLocators.BUTTON_SUBMIT).is_enabled()

    def fill_group_name(self, name_group):
        name = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "name")))
        name.click()
        name.send_keys(name_group, Keys.ENTER)
        return self

    def fill_group_geography(self, geography):
        location = self.driver.find_element(
            *CreateEditGroupsLocators.LOCATION)
        location.click()
        Select(location).select_by_visible_text(geography)
        return self

    def fill_group_owner(self, owner):
        if owner:
            budget_owner = self.driver.find_element(
                *CreateEditGroupsLocators.BUDGET)
            budget_owner.click()
        return self

    def fill_group_direct(self, direct):
        direction = self.driver.find_element(
            *CreateEditGroupsLocators.DIRECTION)
        direction.click()
        Select(direction).select_by_visible_text(direct)
        return self

    def fill_group_first_date(self, first_date):
        start_date = self.driver.find_element(
            *CreateEditGroupsLocators.START_DATE)
        start_date.click()
        start_date.send_keys(first_date)
        return self

    def fill_group_second_date(self, second_date):
        finish_date = self.driver.find_element(
            *CreateEditGroupsLocators.FINISH_DATE)
        finish_date.send_keys(second_date)
        return self

    def fill_group_name_teacher(self, name_teacher):
        teachers = self.driver.find_element(
            *CreateEditGroupsLocators.TEACHERS)
        teachers.click()
        teachers.send_keys(name_teacher)
        return self

    def fill_group_name_experts(self, name_experts):
        expert = self.driver.find_element(
            *CreateEditGroupsLocators.EXPERTS)
        expert.click()
        expert.send_keys(name_experts)
        return self

    def fill_group_level_stage(self, level_stage):
        stage = self.driver.find_element(
            *CreateEditGroupsLocators.STAGE)
        Select(stage).select_by_visible_text(level_stage)
        stage.click()
        return self

    def fill_student_group_id(self, group):
        group_id = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "groupId")))
        group_id.click()
        group_id.send_keys(group, Keys.ENTER)
        return self

    def fill_student_name(self, first_name):
        name = self.driver.find_element(
            *CreateEditStudentsLocators.NAME)
        name.click()
        name.send_keys(first_name)
        return self

    def fill_student_last_name(self, second_name):
        last_name = self.driver.find_element(
            *CreateEditStudentsLocators.LAST_NAME)
        last_name.click()
        last_name.send_keys(second_name)
        return self

    def fill_student_english_level(self, english):
        english_level = self.driver.find_element(
            *CreateEditStudentsLocators.ENGLISH_LEVEL)
        english_level.click()
        Select(english_level).select_by_visible_text(english)
        return self

    def fill_student_cv_url(self, curriculum_vitae):
        cv_url = self.driver.find_element(
            *CreateEditStudentsLocators.CV_URL)
        cv_url.click()
        cv_url.send_keys(curriculum_vitae)
        return self

    def fill_student_image_url(self, image):
        image_url = self.driver.find_element(
            *CreateEditStudentsLocators.IMAGE)
        image_url.click()
        image_url.send_keys(image)
        return self

    def fill_student_entry_score(self, score):
        entry_score = self.driver.find_element(
            *CreateEditStudentsLocators.ENTRY_SCORE)
        entry_score.click()
        entry_score.send_keys(score)
        return self

    def fill_student_approved_by(self, approved):
        approved_by = self.driver.find_element(
            *CreateEditStudentsLocators.APPROVED_BY)
        approved_by.click()
        approved_by.send_keys(approved)
        return self

    def get_table(self, table: str):
        """getting all rows from table"""
        ignored_exceptions = (NoSuchElementException,
                              StaleElementReferenceException)
        WebDriverWait(self.driver, 10, ignored_exceptions=ignored_exceptions). \
            until(EC.presence_of_element_located((By.XPATH, AdminPageLocators.
                                                  get_request_table(table))))
        web_table = self.driver.find_elements(
            By.XPATH, AdminPageLocators.get_request_table(table))
        table_text = [web_element.text for web_element in web_table]
        table = [each.split(',') for each in table_text]
        return table

    def submit(self):
        submit = self.driver.find_element(
            *AdminPageLocators.BUTTON_SUBMIT)
        submit.click()
        return self

    def edit_entity(self):
        pass

    def delete_entity(self):
        pass

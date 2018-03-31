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
        tab_students = self.driver.find_element(*AdminPageLocators.TAB_STUDENTS)
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

    def fill_user_fields(self, name, second_name, type_role, city, photo,
                         log, secret):
        """filling user fields when adding new user"""
        first_name = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "firstName")))
        first_name.click()
        first_name.send_keys(name, Keys.ENTER)
        last_name = self.driver.find_element(
            *CreateEditUsersLocators.LAST_NAME)
        last_name.click()
        last_name.send_keys(second_name)
        role = self.driver.find_element(
            *CreateEditUsersLocators.ROLE)
        role.click()
        Select(role).select_by_visible_text(type_role)
        location = self.driver.find_element(
            *CreateEditUsersLocators.LOCATION)
        location.click()
        Select(location).select_by_visible_text(city)
        login = self.driver.find_element(
            *CreateEditUsersLocators.LOGIN_FIELD)
        login.click()
        login.send_keys(log)
        password = self.driver.find_element(
            *CreateEditUsersLocators.PASSWORD_FIELD)
        password.click()
        password.send_keys(secret)
        submit = self.driver.find_element(
            *AdminPageLocators.BUTTON_SUBMIT)
        submit.click()
        return AdminPage(self.driver)

    def fill_group_fields(self, name_group, geography, owner: False,
                          direct, first_date, second_date, name_teacher,
                          name_experts, level_stage):
        """filling group fields when adding new user"""
        name = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "name")))
        name.click()
        name.send_keys(name_group, Keys.ENTER)
        location = self.driver.find_element(
            *CreateEditGroupsLocators.LOCATION)
        location.click()
        Select(location).select_by_visible_text(geography)
        if owner:
            budget_owner = self.driver.find_element(
                *CreateEditGroupsLocators.BUDGET)
            budget_owner.click()
        direction = self.driver.find_element(
            *CreateEditGroupsLocators.DIRECTION)
        direction.click()
        Select(direction).select_by_visible_text(direct)
        start_date = self.driver.find_element(
            *CreateEditGroupsLocators.START_DATE)
        start_date.click()
        start_date.send_keys(first_date)
        finish_date = self.driver.find_element(
            *CreateEditGroupsLocators.FINISH_DATE)
        finish_date.send_keys(second_date)
        teachers = self.driver.find_element(
            *CreateEditGroupsLocators.TEACHERS)
        teachers.click()
        teachers.send_keys(name_teacher)
        expert = self.driver.find_element(
            *CreateEditGroupsLocators.EXPERTS)
        expert.click()
        expert.send_keys(name_experts)
        stage = self.driver.find_element(
            *CreateEditGroupsLocators.STAGE)
        Select(stage).select_by_visible_text(level_stage)
        stage.click()
        submit = self.driver.find_element(
            *AdminPageLocators.BUTTON_SUBMIT)
        submit.click()
        return AdminPage(self.driver)

    def fill_student_fields(self, group, first_name, second_name, english,
                            curriculum_vitae, image, score, approved):
        """filling student fields when adding new user"""
        group_id = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "groupId")))
        group_id.click()
        group_id.send_keys(group, Keys.ENTER)
        name = self.driver.find_element(
            *CreateEditStudentsLocators.NAME)
        name.click()
        name.send_keys(first_name)
        last_name = self.driver.find_element(
            *CreateEditStudentsLocators.LAST_NAME)
        last_name.click()
        last_name.send_keys(second_name)
        english_level = self.driver.find_element(
            *CreateEditStudentsLocators.ENGLISH_LEVEL)
        english_level.click()
        Select(english_level).select_by_visible_text(english)
        english_level.click()
        cv_url = self.driver.find_element(
            *CreateEditStudentsLocators.CV_URL)
        cv_url.click()
        cv_url.send_keys(curriculum_vitae)
        image_url = self.driver.find_element(
            *CreateEditStudentsLocators.IMAGE)
        image_url.click()
        image_url.send_keys(image)
        entry_score = self.driver.find_element(
            *CreateEditStudentsLocators.ENTRY_SCORE)
        entry_score.click()
        entry_score.send_keys(score)
        approved_by = self.driver.find_element(
            *CreateEditStudentsLocators.APPROVED_BY)
        approved_by.click()
        approved_by.send_keys(approved)
        submit = self.driver.find_element(
            *AdminPageLocators.BUTTON_SUBMIT)
        submit.click()
        return AdminPage(self.driver)

    def get_table(self, table: str):
        """getting all row from table"""
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
        wait_table = WebDriverWait(
            self.driver, 5, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located((
                By.XPATH, AdminPageLocators.get_request_table(table))))
        web_table = self.driver.find_elements(
            By.XPATH, AdminPageLocators.get_request_table(table))
        table_text = [web_element.text for web_element in web_table]
        actual_result = [each.split(',') for each in table_text]
        return actual_result

    def edit_entity(self):
        pass

    def delete_entity(self):
        pass
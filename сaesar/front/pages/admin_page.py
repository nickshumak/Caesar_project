from front.locators.locators import AdminPageLocators, \
    CreateEditUsersLocators, CreateEditGroupsLocators, \
    CreateEditStudentsLocators
from front.pages.base_page import BasePage
from front.pages.groups_page import GroupsPage
from selenium.webdriver.support.ui import Select


class AdminPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def tab_users(self):
        tab_users = self.driver.find_element(*AdminPageLocators.TAB_USERS)
        tab_users.click()
        return self

    def tab_groups(self):
        tab_groups = self.driver.find_element(*AdminPageLocators.TAB_GROUPS)
        tab_groups.click()
        return self

    def tab_students(self):
        tab_students = self.driver.find_element(*AdminPageLocators.TAB_STUDENTS)
        tab_students.click()
        return self

    def add_entity(self):
        add_entity = self.driver.find_element(*AdminPageLocators.ADD_ENTITY)
        add_entity.click()

    def back_home(self):
        back_home = self.driver.find_element(*AdminPageLocators.BUTTON_ESCAPE)
        back_home.click()
        return GroupsPage(self.driver)

    def fill_fields_users(self):
        first_name = self.driver.find_element(
            *CreateEditUsersLocators.FIRST_NAME)
        first_name.click()
        first_name.send_keys('ТУТ ТЕКСТ')
        last_name = self.driver.find_element(
            *CreateEditUsersLocators.LAST_NAME)
        last_name.click()
        last_name.send_key("TEXT!!!!")
        role = self.driver.find_element(
            *CreateEditUsersLocators.ROLE)
        role.click()
        Select(role).select_by_visible_text("TEXT")
        location = self.driver.find_element(
            *CreateEditUsersLocators.LOCATION)
        location.click()
        Select(location).select_by_visible_text('Dnipro')
        login = self.driver.find_element(
            *CreateEditUsersLocators.LOGIN_FIELD)
        login.click()
        login.send_key("TEXT")
        password = self.driver.find_element(
            *CreateEditUsersLocators.PASSWORD_FIELD)
        password.click()
        password.send_keys("TEXT")
        submit = self.driver.find_element(*CreateEditUsersLocators.BUTTON_SUBMIT)
        submit.click()

    def fill_fields_groups(self):
        name = self.driver.find_element(*CreateEditGroupsLocators.NAME)
        name.click()
        name.send_keys("TEXT")
        location = self.driver.find_element(*CreateEditGroupsLocators.LOCATION)
        location.click()
        Select(location).select_by_visible_text("TEXT")
        budget_owner = self.driver.find_element(*CreateEditGroupsLocators.BUDGET)
        budget_owner.click()
        direction = self.driver.find_element(*CreateEditGroupsLocators.DIRECTION)
        direction.click()
        print("VIBOR NAPRAVLENIYA")
        #
        start_date = self.driver.find_element(*CreateEditGroupsLocators.START_DATE)
        start_date.click()
        start_date.clear()
        start_date.send_keys("TEXT")
        # 1993-12-01
        finish_date = self.driver.find_element(*CreateEditGroupsLocators.FINISH_DATE)
        finish_date.clear()
        finish_date.send_keys("TEXT")
        # 0199-12-12
        teachers = self.driver.find_element(*CreateEditGroupsLocators.TEACHERS)
        teachers.click()
        teachers.send_keys('text')
        stage = self.driver.find_element(*CreateEditGroupsLocators.STAGE)
        Select(stage).select_by_visible_text('TEXT!!!')
        stage.click()
        # надо тут клик или нет хз
        submit = self.driver.find_element(*CreateEditGroupsLocators.BUTTON_SUBMIT)
        submit.click()

    def fill_fields_students(self):
        group_id = self.driver.find_element(*CreateEditStudentsLocators.GROUP_ID)
        group_id.click()
        group_id.send_keys("TEXT")
        name = self.driver.find_element(*CreateEditStudentsLocators.NAME)
        name.click()
        name.send_keys("TEXT")
        last_name = self.driver.find_element(*CreateEditStudentsLocators.LAST_NAME)
        last_name.click()
        last_name.send_keys('TEXT')
        english_level = self.driver.find_element(*CreateEditStudentsLocators.ENGLISH_LEVEL)
        english_level.click()
        Select(english_level).select_by_visible_text('LVL ')
        english_level.click()
        cv_url = self.driver.find_element(*CreateEditStudentsLocators.CV_URL)
        cv_url.click()
        cv_url.send_keys("TEXT")
        entry_score = self.driver.find_element(*CreateEditStudentsLocators.ENTRY_SCORE)
        entry_score.click()
        entry_score.send_keys("TEXT")
        approved_by = self.driver.find_element(*CreateEditStudentsLocators.APPROVED_BY)
        approved_by.click()
        approved_by.send_text("TEXT")
        submit = self.driver.find_element(*CreateEditStudentsLocators.BUTTON_SUBMIT)
        submit.click()

    def edit_entity(self):
        pass

    def delete_entity(self):
        pass

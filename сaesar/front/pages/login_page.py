from front.locators.locators import *
from front.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from front.pages.groups_page import GroupsPage


class LogInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def user_name(self, name_user):
        name_field = self.driver.find_element(
            *LogInLocators.LOGIN_FIELD)
        name_field.click()
        name_field.clear()
        name_field.send_keys(name_user, Keys.ENTER)
        return self

    def user_password(self, password_user):
        password_field = self.driver.find_element(
            *LogInLocators.PASSWORD_FIELD)
        password_field.click()
        password_field.clear()
        password_field.send_keys(password_user, Keys.ENTER)
        return self

    def submit_log_in(self):
        submit_btn = lambda: self.driver.find_element(
            *LogInLocators.CONFIRM_ACTION).click()
        return GroupsPage(self.driver)

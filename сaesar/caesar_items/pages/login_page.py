from caesar_items.pages.base_page import BasePage
from caesar_items.locators.locators import *
from caesar_items.pages.groups_page import GroupsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class LogInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_login(self, user_login=''):
        self.driver.find_element(*LogInLocators.LOGIN_FIELD).clear()
        return self.driver.find_element(*LogInLocators.LOGIN_FIELD).\
            send_keys(user_login)

    def enter_password(self, user_password=''):
        self.driver.find_element(*LogInLocators.PASSWORD_FIELD).clear()
        return self.driver.find_element(*LogInLocators.PASSWORD_FIELD).\
            send_keys(user_password)

    def message(self):
        return self.driver.find_element(*LogInLocators.FIELD_MESSAGE).text

    def submit_button_element(self):
        return self.driver.find_element(*LogInLocators.CONFIRM_ACTION)

    def open_group_page(self):
        self.driver.find_element(*LogInLocators.CONFIRM_ACTION).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(GroupPageLocators.USER_PHOTO))
        return GroupsPage(self.driver)

    def auto_login(self, user):
        self.enter_login(user.login)
        self.enter_password(user.password)
        self.open_group_page()

    def login_use_tab_n_enter_keys(self, user):
        ActionChains(self.driver).send_keys(user.login).send_keys(Keys.TAB) \
            .send_keys(user.password).send_keys(Keys.ENTER).perform()
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(GroupPageLocators.USER_PHOTO))
        return GroupsPage(self.driver)




from front.pages.base_page import BasePage
from front.locators.locators import LogInLocators
# from page_objects import PageObject, PageElement


# class LogInPage(PageObject, BasePage):
#     login = PageElement(name='login')
#     password = PageElement(name='password')
#     submit = PageElement(tag_name='button')
#     massage = PageElement(class_name='message')


class LogInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_url(self):
        self.driver.get('http://localhost:3000')

    def log_in_visitor(self, visitor):
        self.driver.find_element(*LogInLocators.LOGIN_FIELD).send_keys(visitor.login)
        self.driver.find_element(*LogInLocators.PASSWORD_FIELD).send_keys(visitor.password)
        self.driver.find_element(*LogInLocators.CONFIRM_ACTION).click()
        return self

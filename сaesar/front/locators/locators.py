from selenium.webdriver.common.by import By


class LogInLocators(object):
    LOGIN_FIELD = (By.NAME, 'login')
    PASSWORD_FIELD = (By.NAME, 'password')
    TEXT_FIELD = (By.CLASS_NAME, 'message')
    CONFIRM_ACTION = (By.ID, "")

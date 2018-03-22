from front.pages.base_page import BasePage
from page_objects import PageObject, PageElement


class LogInPage(PageObject, BasePage):
    login = PageElement(name='login')
    password = PageElement(name='password')
    submit = PageElement(css='body > div.app > div > div > div > button')
    massage = PageElement(class_name='message')

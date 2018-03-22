import unittest
from selenium import webdriver
from resource.url_site import PathUrl
from resource.path_driver import GetDriver
from front.pages.login_page import LogInPage


class TestBase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=GetDriver().DRIVER_CHROME)
        self.login_page = LogInPage(self.driver)
        self.login_page.get(PathUrl().URL_SITE)

    def tearDown(self):
        self.driver.quit()

from tests.test_base import TestBase
from front.pages.login_page import LogInPage
from front.pages.groups_page import GroupsPage
import time

import unittest


class TestLog(TestBase):
    #
    # def test_login_in(self):
    #     """проверку добавить на факт нужной страницы"""
    #     groups_page = LogInPage(self.driver) \
    #         .user_name("dmytro") \
    #         .user_password('1234') \
    #         .submit_log_in().get_title_name()
    #     self.assertIn("Caesar", groups_page)
    #     time.sleep(5)

    def test_2(self):
        """проверку добавить на факт нужной страницы"""
        groups_page = LogInPage(self.driver) \
            .user_name("dmytro") \
            .user_password('1234') \
            .submit_log_in().get_title_name()
        time.sleep(5)
        groups_page = groups_page.click_button_search()
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()

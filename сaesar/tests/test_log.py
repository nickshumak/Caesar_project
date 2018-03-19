from tests.test_base import TestBase
from front.pages.login_page import LogInPage

import unittest


class TestLog(TestBase):

    def test_login_in(self):
        groups_page = LogInPage(self.driver)\
            .user_name("dmytro")\
            .user_password('1234')\
            .submit_log_in()


if __name__ == '__main__':
    unittest.main()

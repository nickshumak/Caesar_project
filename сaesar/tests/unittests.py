from resource.users_base import *
from tests.test_base import TestBase


expected_page_title = 'Caesar'
group_name = 'DP-098-JS'


class TestCustomFunctions(TestBase):

    def test_auto_login_function(self):
        """ Check custom login function working that get user as parameter."""
        group_page = self.login_page.auto_login(first_admin)
        self.assertEqual(group_page.get_title_name(), expected_page_title)

    def test_creating_group_test(self):
        """ Check creating group function is working."""
        group_page = self.login_page.auto_login(first_admin)
        left_menu = group_page.open_left_menu()
        left_menu.create_group_button().click()
        group_page.CreateGroupWindow().auto_fill_all_fields(
            group_name, first_admin.location)
        self.driver.quit()

    def test_creating_users_function(self):
        """ Check creating new users for testing function is working."""
        group_page = self.login_page.auto_login(first_admin)
        group_page.open_admin_page()
        create_8_users_for_tests(self.driver)
        self.driver.quit()

from resource.users_base import *
from tests.test_base import TestBase
from resource.error_handler import logger_exception


class TestLocationWindow(TestBase):
    def setUp(self):
        super().setUp()
        self.group_page = self.login_page.auto_login(first_admin)
        self.top_menu = self.group_page.open_top_menu()
        self.locations_window = self.top_menu.click_locations_button()

    @logger_exception
    def test01_save_button_disabled(self):
        """ Check that save button disabled when no one location
         was selected."""
        self.assertFalse(self.locations_window.disabled_save_button().
                         is_enabled())

    @logger_exception
    def test02_return_group_page_using_cancel_button(self):
        """ Check that when user click cancel button, group page will
        be opened."""
        expected_url = 'http://localhost:3000/Groups/Dnipro'
        self.locations_window.cancel_button().click()
        self.assertEqual(self.locations_window.get_current_url(), expected_url)

    @logger_exception
    def test03_select_one_location(self):
        """ Check that user can select location."""
        expected_result = 'Dnipro'
        self.locations_window.select_dnipro_location()
        self.locations_window.save_button().click()
        actual_result = self.group_page.get_group_location_text()
        self.assertEqual(actual_result, expected_result)

    @logger_exception
    def test04_select_two_locations(self):
        """ Check that user can select several locations."""
        expected_result = '2 locations'
        self.locations_window.select_dnipro_location()\
            .select_kyiv_location()\
            .save_button().click()
        actual_result = self.group_page.get_group_location_text()
        self.assertEqual(actual_result, expected_result)

    @logger_exception
    def test05_select_all_locations(self):
        """ Check that user can select all locations."""
        expected_result = '7 locations'
        self.locations_window.select_dnipro_location()\
            .select_kyiv_location()\
            .select_chernivtsy_location()\
            .select_ivano_frankivsk_location()\
            .select_lviv_location()\
            .select_rivne_location()\
            .select_sofia_location()
        self.locations_window.save_button().click()
        actual_result = self.group_page.get_group_location_text()
        self.assertEqual(actual_result, expected_result)

    @logger_exception
    def test06_uncheck_location(self):
        """ Check that user can uncheck selected locations."""
        expected_result = 'Dnipro'
        self.locations_window.select_dnipro_location()\
            .select_kyiv_location()
        self.locations_window.save_button().click()
        top_menu = self.group_page.open_top_menu()
        top_menu.click_locations_button()
        self.locations_window.select_kyiv_location()
        self.locations_window.save_button().click()
        actual_result = self.group_page.get_group_location_text()
        self.assertEqual(actual_result, expected_result)

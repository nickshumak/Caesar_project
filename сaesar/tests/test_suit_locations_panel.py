from resource.users_base import *
from tests.test_base import TestBase


class TestLocationWindow(TestBase):
    def setUp(self):
        super().setUp()
        self.group_page = self.login_page.auto_login(first_admin)
        self.top_menu = self.group_page.open_top_menu()
        self.locations_window = self.top_menu.click_locations_button()

    def test01_save_button_disabled(self):
        """
        check that save button disabled when no one location was selected
        """
        self.assertFalse(self.locations_window.disabled_save_button().is_enabled())

    def test02_return_group_page_using_cancel_button(self):
        """
        check that when user click cancel button, group page will be opened
        """
        expected_url = 'http://localhost:3000/Groups/Dnipro'
        self.locations_window.cancel_button().click()
        self.assertEqual(self.locations_window.get_current_url(), expected_url)

    def test03_select_one_location(self):
        """
        check that user can select location
        """
        location_name = 'Dnipro'
        self.locations_window.select_dnipro_location()
        self.locations_window.save_button().click()
        actual_result = self.group_page.get_group_location_text()
        self.assertEqual(actual_result, location_name)

    def test03_two_locations(self):
        """
        check that user can select several locations
        """
        locations_name = '2 locations'
        self.locations_window.select_dnipro_location()
        self.locations_window.select_kyiv_location()
        self.locations_window.save_button().click()
        actual_result = self.group_page.get_group_location_text()
        self.assertEqual(actual_result, locations_name)

    def test04_select_all_locations(self):
        """
        check that user can select all locations
        """
        locations_name = '7 locations'
        self.locations_window.select_dnipro_location()
        self.locations_window.select_kyiv_location()
        self.locations_window.select_chernivtsy_location()
        self.locations_window.select_ivano_frankivsk_location()
        self.locations_window.select_lviv_location()
        self.locations_window.select_rivne_location()
        self.locations_window.select_sofia_location()

        self.locations_window.save_button().click()
        actual_result = self.group_page.get_group_location_text()
        self.assertEqual(actual_result, locations_name)

    def test05_uncheck_location(self):
        """
        check that user can uncheck selected locations
        """
        location_name = 'Dnipro'
        self.locations_window.select_dnipro_location()
        self.locations_window.select_kyiv_location()
        self.locations_window.save_button().click()
        top_menu = self.group_page.open_top_menu()
        top_menu.click_locations_button()
        self.locations_window.select_kyiv_location()
        self.locations_window.save_button().click()
        actual_result = self.group_page.get_group_location_text()
        self.assertEqual(actual_result, location_name)

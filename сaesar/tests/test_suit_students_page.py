"""
Tests check the additional, removal and editing of
student data, adding cv_files and photo in the list of students
with different roles(administrator, coordinator, teacher)
"""

import unittest
from selenium import webdriver
from resource.url_site import PathUrl
from resource.path_driver import GetDriver
from caesar_items.pages.login_page import LogInPage
from caesar_items.pages.groups_page import GroupsPage
from caesar_items.pages.students_page import StudentsPage, Student, \
    data_student_for_check, sorted_students_list, remove_none_from_list
from resource.users_base import first_admin, coordinator, teacher

# main url for tests
url_for_test_start = 'http://localhost:3000/Students/Dnipro/DP-093-JS/'

# expected variables
expected_url = 'http://localhost:3000/Students/Dnipro/DP-093-JS/list'
expected_name_file_cv = 'cv.docx'
expected_name_file_photo = 'photo.jpg'
group_name = 'DP-093-JS'
expected_warnings = ['You can use only letters, space and "-"',
                     'You can use only letters, space and "-"',
                     'You can use only letters, space and "-"',
                     'You can use only letters, space and "-"',
                     'You can use only letters, space and "-"',
                     'You can use only letters, space and "-"']

# data for adding new student
first_new_student = Student(first_name='Vladyslava', last_name='Semmi',
                            incoming_mark='111', entry_mark='5')
second_new_student = Student('Sherlock', 'Holmes', '333', '3')
third_new_student = Student('Merlin', 'Monro', '123', '3')

# data for editing student
first_new_data_student = Student('Garry', 'Potter', '222', '2')
second_new_data_student = Student('Robin', 'Good', '444', '4')
third_new_data_student = Student('Clark', 'Kent', '321', '3')

# path for files
path_file_cv = "..\\resource\cv.docx"
path_file_photo = "..\\resource\photo.jpg"


class TestStudentsPageWithAdmin(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=GetDriver().CHROME_DRIVER)
        cls.driver.get(PathUrl().SITE_URL)
        cls.driver.maximize_window()
        cls.login_page = LogInPage(cls.driver)
        cls.login_page.auto_login(first_admin)
        cls.main_page = GroupsPage(cls.driver)
        cls.main_page.open_top_menu()
        cls.main_page.top_menu.click_students_button()
        cls.main_page.select_group_by_name(group_name)
        cls.students_page = StudentsPage(cls.driver)
        return cls.students_page

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.students_page.driver.get(url_for_test_start)
        self.students_page.driver.implicitly_wait(2)

    def test01_add_new_student_with_admin(self):
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_add_new_student_button()
        self.students_page.students_list.student_data.\
            enter_student_data(first_new_student)
        self.students_page.students_list.student_data.\
            click_save_data_changes_button()
        self.students_page.students_list.\
            click_exit_editor_students_list_button()
        student = data_student_for_check(first_new_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.main_page.get_current_url(),
                         expected_url)
        self.assertIn(student, students_list)

    def test02_edit_data_first_student_with_admin(self):
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_edit_student_button()
        self.students_page.students_list.student_data.\
            enter_student_data(first_new_data_student)
        self.students_page.students_list.student_data.\
            click_save_data_changes_button()
        self.students_page.students_list.\
            click_exit_editor_students_list_button()
        student_with_changes = \
            data_student_for_check(first_new_data_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.main_page.get_current_url(),
                         expected_url)
        self.assertIn(student_with_changes, students_list)

    def test03_edit_cv_first_student_with_admin(self):
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_edit_student_button()
        self.students_page.students_list.student_data.add_cv(path_file_cv)
        actual_name_file = self.students_page.\
            students_list.student_data.get_name_cv_file()
        self.assertEqual(actual_name_file, expected_name_file_cv)

    def test04_edit_photo_first_student_with_admin(self):
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_edit_student_button()
        self.students_page.students_list.student_data.\
            add_photo(path_file_photo)
        actual_name_file = self.students_page.students_list.\
            student_data.get_name_photo_file()
        self.assertEqual(actual_name_file, expected_name_file_photo)

    def test05_students_list_sort_by_name(self):
        unsorted_students_list = self.students_page.students_table()
        self.students_page.students_list.\
            click_students_list_sort_by_name_button()
        # get sorted list with button without None
        sorted_list_by_button = \
            remove_none_from_list(self.students_page.students_table())
        # get sorted list with function without None
        sorted_list_by_function = \
            remove_none_from_list(sorted_students_list(unsorted_students_list))
        self.assertEqual(sorted_list_by_button, sorted_list_by_function)

    def test06_add_student_with_empty_fields(self):
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_add_new_student_button()
        self.students_page.students_list.student_data.\
            click_save_data_changes_button()
        actual_warnings = self.students_page.students_list.student_data. \
            warnings_text_for_adding_student_with_empty_fields()
        self.assertEqual(actual_warnings, expected_warnings)

    def test07_remove_first_student_with_admin(self):
        first_student = self.students_page.students_table()[0]
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.\
            click_delete_first_student_button()
        self.students_page.students_list.\
            click_exit_editor_students_list_button()
        students_list = self.students_page.students_table()
        self.assertEqual(self.main_page.get_current_url(),
                         expected_url)
        self.assertNotIn(first_student, students_list)


class TestStudentsPageWithCoordinator(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=GetDriver().CHROME_DRIVER)
        cls.driver.get(PathUrl().SITE_URL)
        cls.driver.maximize_window()
        cls.login_page = LogInPage(cls.driver)
        cls.login_page.auto_login(coordinator)
        cls.main_page = GroupsPage(cls.driver)
        cls.main_page.open_top_menu()
        cls.main_page.top_menu.click_students_button()
        cls.main_page.select_group_by_name(group_name)
        cls.students_page = StudentsPage(cls.driver)
        return cls.students_page

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.students_page.driver.get(url_for_test_start)
        self.students_page.driver.implicitly_wait(2)

    def test08_add_new_student_with_coordinator(self):
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_add_new_student_button()
        self.students_page.students_list.student_data.\
            enter_student_data(second_new_student)
        self.students_page.students_list.student_data.\
            click_save_data_changes_button()
        self.students_page.students_list.\
            click_exit_editor_students_list_button()
        student = data_student_for_check(second_new_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.main_page.get_current_url(),
                         expected_url)
        self.assertIn(student, students_list)

    def test09_edit_data_first_student_with_coordinator(self):
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_edit_student_button()
        self.students_page.students_list.student_data.\
            enter_student_data(second_new_data_student)
        self.students_page.students_list.student_data.\
            click_save_data_changes_button()
        self.students_page.students_list.\
            click_exit_editor_students_list_button()
        student_with_changes = \
            data_student_for_check(second_new_data_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.main_page.get_current_url(),
                         expected_url)
        self.assertIn(student_with_changes, students_list)

    def test10_edit_cv_first_student_with_coordinator(self):
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_edit_student_button()
        self.students_page.students_list.student_data.add_cv(path_file_cv)
        actual_name_file = self.students_page.\
            students_list.student_data.get_name_cv_file()
        self.assertEqual(actual_name_file, expected_name_file_cv)

    def test11_edit_photo_first_student_with_coordinator(self):
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_edit_student_button()
        self.students_page.students_list.student_data.\
            add_photo(path_file_photo)
        actual_name_file = self.students_page.students_list.\
            student_data.get_name_photo_file()
        self.assertEqual(actual_name_file, expected_name_file_photo)

    def test12_remove_first_student_with_coordinator(self):
        first_student = self.students_page.students_table()[0]
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list. \
            click_delete_first_student_button()
        self.students_page.students_list. \
            click_exit_editor_students_list_button()
        students_list = self.students_page.students_table()
        self.assertEqual(self.main_page.get_current_url(),
                         expected_url)
        self.assertNotIn(first_student, students_list)


class TestStudentsPageWithTeacher(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=GetDriver().CHROME_DRIVER)
        cls.driver.get(PathUrl().SITE_URL)
        cls.driver.maximize_window()
        cls.login_page = LogInPage(cls.driver)
        cls.login_page.auto_login(teacher)
        cls.main_page = GroupsPage(cls.driver)
        cls.main_page.open_top_menu()
        cls.main_page.top_menu.click_students_button()
        cls.main_page.select_group_by_name(group_name)
        cls.students_page = StudentsPage(cls.driver)
        return cls.students_page

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.students_page.driver.get(url_for_test_start)
        self.students_page.driver.implicitly_wait(2)

    def test13_add_new_student_with_teacher(self):
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_add_new_student_button()
        self.students_page.students_list.student_data.\
            enter_student_data(third_new_student)
        self.students_page.students_list.student_data.\
            click_save_data_changes_button()
        self.students_page.students_list.\
            click_exit_editor_students_list_button()
        student = data_student_for_check(third_new_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.main_page.get_current_url(),
                         expected_url)
        self.assertIn(student, students_list)

    def test14_edit_data_first_student_with_teacher(self):
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_edit_student_button()
        self.students_page.students_list.student_data.\
            enter_student_data(third_new_data_student)
        self.students_page.students_list.student_data.\
            click_save_data_changes_button()
        self.students_page.students_list.\
            click_exit_editor_students_list_button()
        student_with_changes = \
            data_student_for_check(third_new_data_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.main_page.get_current_url(),
                         expected_url)
        self.assertIn(student_with_changes, students_list)

    def test15_edit_cv_first_student_with_teacher(self):
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_edit_student_button()
        self.students_page.students_list.student_data.add_cv(path_file_cv)
        actual_name_file = self.students_page.\
            students_list.student_data.get_name_cv_file()
        self.assertEqual(actual_name_file, expected_name_file_cv)

    def test16_edit_photo_first_student_with_teacher(self):
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_edit_student_button()
        self.students_page.students_list.student_data.\
            add_photo(path_file_photo)
        actual_name_file = self.students_page.students_list.\
            student_data.get_name_photo_file()
        self.assertEqual(actual_name_file, expected_name_file_photo)

    def test17_remove_first_student_with_teacher(self):
        first_student = self.students_page.students_table()[0]
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list. \
            click_delete_first_student_button()
        self.students_page.students_list. \
            click_exit_editor_students_list_button()
        students_list = self.students_page.students_table()
        self.assertEqual(self.main_page.get_current_url(),
                         expected_url)
        self.assertNotIn(first_student, students_list)


if __name__ == '__main__':
    unittest.main()


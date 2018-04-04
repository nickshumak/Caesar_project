"""
Tests check the adding, removal and editing of
student data, adding cv_files and photo in the list of students
with different roles(administrator, coordinator, teacher),
also check the opportunity of adding new student with empty data and
sorting student's list by name.
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
expected_url_group_info = 'http://localhost:3000/Groups/Dnipro/DP-093-JS/info'

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
                            incoming_mark='111', entry_mark='5',
                            english_level='Pre-intermediate',
                            approved_by='Not approved')
second_new_student = Student('Sherlock', 'Holmes', '333', '3',
                             'Pre-intermediate strong', 'N. Varenko')
third_new_student = Student('Merlin', 'Monro', '123', '3', 'Elementary',
                            'Custom', 'Casper')

# data for editing student
first_new_data_student = Student('Garry', 'Potter', '222', '2',
                                 'Upper-intermediate', 'Not approved')
second_new_data_student = Student('Robin', 'Good', '444', '4',
                                  'Advanced', 'N. Varenko')
third_new_data_student = Student('Clark', 'Kent', '321', '3',
                                 'Upper-intermediate low',
                                 'Custom', 'Casper')

# file's path
path_file_cv = "..\\resource\cv.docx"
path_file_photo = "..\\resource\photo.jpg"


class TestStudentsPageWithAdmin(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        """Log in by administrator, open top menu,select
        button 'students', select group."""
        cls.driver = webdriver.Chrome(
            executable_path=GetDriver().DRIVER_CHROME)
        cls.driver.get(PathUrl().URL_SITE)
        cls.driver.maximize_window()
        cls.login_page = LogInPage(cls.driver)
        cls.login_page.auto_login(first_admin)
        cls.main_page = GroupsPage(cls.driver)
        cls.main_page.open_top_menu()
        cls.main_page.top_menu.students()
        cls.main_page.select_group(group_name)
        cls.students_page = StudentsPage(cls.driver)
        return cls.students_page

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.students_page.driver.get(url_for_test_start)
        self.students_page.driver.implicitly_wait(2)

    def test01_add_new_student_with_admin(self):
        """Check is new student added by administrator."""
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_add_new_student_button()
        self.students_page.students_list.student_data. \
            enter_student_data(first_new_student)
        self.students_page.students_list.student_data. \
            click_save_data_changes_button()
        self.students_page.students_list. \
            click_exit_students_list_editor_button()
        student = data_student_for_check(first_new_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.main_page.get_current_url(),
                         expected_url)
        self.assertIn(student, students_list)

    def test02_edit_data_first_student_with_admin(self):
        """Check is first student editing by administrator."""
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_edit_student_button()
        self.students_page.students_list.student_data. \
            enter_student_data(first_new_data_student)
        self.students_page.students_list.student_data. \
            click_save_data_changes_button()
        self.students_page.students_list. \
            click_exit_students_list_editor_button()
        student_with_changes = \
            data_student_for_check(first_new_data_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.main_page.get_current_url(),
                         expected_url)
        self.assertIn(student_with_changes, students_list)

    def test03_edit_cv_first_student_with_admin(self):
        """Check is cv file added to the student's data
        by administrator."""
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_edit_student_button()
        self.students_page.students_list.student_data.add_cv(path_file_cv)
        actual_name_file = self.students_page. \
            students_list.student_data.get_name_cv_file()
        self.assertEqual(actual_name_file, expected_name_file_cv)

    def test04_edit_photo_first_student_with_admin(self):
        """Check is photo file added to the student's data
        by administrator."""
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_edit_student_button()
        self.students_page.students_list.student_data. \
            add_photo(path_file_photo)
        actual_name_file = self.students_page.students_list. \
            student_data.get_name_photo_file()
        self.assertEqual(actual_name_file, expected_name_file_photo)

    def test05_students_list_sort_by_name(self):
        """Check with role administrator is student's list sorting by name."""
        unsorted_students_list = self.students_page.students_table()
        self.students_page.students_list. \
            click_students_list_sort_by_name_button()
        # get sorted list with button without None
        sorted_list_by_button = \
            remove_none_from_list(self.students_page.students_table())
        # get sorted list with function without None
        sorted_list_by_function = \
            remove_none_from_list(sorted_students_list(unsorted_students_list))
        self.assertEqual(sorted_list_by_button, sorted_list_by_function)

    def test06_add_student_with_empty_fields(self):
        """Check adding new student with empty fields by administrator"""
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_add_new_student_button()
        self.students_page.students_list.student_data. \
            click_save_data_changes_button()
        actual_warnings = self.students_page.students_list.student_data. \
            warnings_text_for_adding_student_with_empty_fields()
        self.assertEqual(actual_warnings, expected_warnings)

    def test07_remove_first_student_with_admin(self):
        """Check deleting first student from the student's list
        by administrator."""
        first_student = self.students_page.students_table()[0]
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list. \
            click_delete_first_student_button()
        self.students_page.students_list. \
            click_exit_students_list_editor_button()
        students_list = self.students_page.students_table()
        self.assertEqual(self.main_page.get_current_url(),
                         expected_url)
        self.assertNotIn(first_student, students_list)

    def test08_add_equal_students_with_admin(self):
        """Check opportunity of adding two equal students by administrator."""
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_add_new_student_button()
        self.students_page.students_list.student_data. \
            enter_student_data(first_new_student)
        self.students_page.students_list.student_data. \
            click_save_data_changes_button()
        self.students_page.students_list.click_add_new_student_button()
        self.students_page.students_list.student_data. \
            enter_student_data(first_new_student)
        self.students_page.students_list.student_data. \
            click_save_data_changes_button()
        # save data changes button have not to be enabled for
        # adding two equal students
        self.assertTrue(self.students_page.students_list.student_data.
                        save_data_changes_button().is_enabled())


class TestStudentsPageWithCoordinator(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        """Log in by coordinator, open top menu,select
        button 'students', select group."""
        cls.driver = webdriver.Chrome(
            executable_path=GetDriver().DRIVER_CHROME)
        cls.driver.get(PathUrl().URL_SITE)
        cls.driver.maximize_window()
        cls.login_page = LogInPage(cls.driver)
        cls.login_page.auto_login(coordinator)
        cls.main_page = GroupsPage(cls.driver)
        cls.main_page.open_top_menu()
        cls.main_page.top_menu.students()
        cls.main_page.select_group(group_name)
        cls.students_page = StudentsPage(cls.driver)
        return cls.students_page

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.students_page.driver.get(url_for_test_start)
        self.students_page.driver.implicitly_wait(2)

    def test09_add_new_student_with_coordinator(self):
        """Check is new student added by coordinator."""
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_add_new_student_button()
        self.students_page.students_list.student_data. \
            enter_student_data(second_new_student)
        self.students_page.students_list.student_data. \
            click_save_data_changes_button()
        self.students_page.students_list. \
            click_exit_students_list_editor_button()
        student = data_student_for_check(second_new_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.main_page.get_current_url(),
                         expected_url)
        self.assertIn(student, students_list)

    def test10_edit_data_first_student_with_coordinator(self):
        """Check is first student editing by coordinator."""
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_edit_student_button()
        self.students_page.students_list.student_data. \
            enter_student_data(second_new_data_student)
        self.students_page.students_list.student_data. \
            click_save_data_changes_button()
        self.students_page.students_list. \
            click_exit_students_list_editor_button()
        student_with_changes = \
            data_student_for_check(second_new_data_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.main_page.get_current_url(),
                         expected_url)
        self.assertIn(student_with_changes, students_list)

    def test11_edit_cv_first_student_with_coordinator(self):
        """Check is cv file added to the student's data
        by coordinator."""
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_edit_student_button()
        self.students_page.students_list.student_data.add_cv(path_file_cv)
        actual_name_file = self.students_page. \
            students_list.student_data.get_name_cv_file()
        self.assertEqual(actual_name_file, expected_name_file_cv)

    def test12_edit_photo_first_student_with_coordinator(self):
        """Check is photo file added to the student's data
        by coordinator."""
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_edit_student_button()
        self.students_page.students_list.student_data. \
            add_photo(path_file_photo)
        actual_name_file = self.students_page.students_list. \
            student_data.get_name_photo_file()
        self.assertEqual(actual_name_file, expected_name_file_photo)

    def test13_remove_first_student_with_coordinator(self):
        """Check deleting first student from the student's list
        by coordinator."""
        first_student = self.students_page.students_table()[0]
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list. \
            click_delete_first_student_button()
        self.students_page.students_list. \
            click_exit_students_list_editor_button()
        students_list = self.students_page.students_table()
        self.assertEqual(self.main_page.get_current_url(),
                         expected_url)
        self.assertNotIn(first_student, students_list)


class TestStudentsPageWithTeacher(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        """Log in by teacher, open top menu,select
        button 'students', select group."""
        cls.driver = webdriver.Chrome(
            executable_path=GetDriver().DRIVER_CHROME)
        cls.driver.get(PathUrl().URL_SITE)
        cls.driver.maximize_window()
        cls.login_page = LogInPage(cls.driver)
        cls.login_page.auto_login(teacher)
        cls.main_page = GroupsPage(cls.driver)
        cls.main_page.open_top_menu()
        cls.main_page.top_menu.students()
        cls.main_page.select_group(group_name)
        cls.students_page = StudentsPage(cls.driver)
        return cls.students_page

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.students_page.driver.get(url_for_test_start)
        self.students_page.driver.implicitly_wait(2)

    def test14_add_new_student_with_teacher(self):
        """Check is new student added by teacher."""
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_add_new_student_button()
        self.students_page.students_list.student_data. \
            enter_student_data(third_new_student)
        self.students_page.students_list.student_data.\
            enter_name_approved_by_custom(third_new_student.
                                          approved_by_custom)
        self.students_page.students_list.student_data. \
            click_save_data_changes_button()
        self.students_page.students_list. \
            click_exit_students_list_editor_button()
        student = data_student_for_check(third_new_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.main_page.get_current_url(),
                         expected_url)
        self.assertIn(student, students_list)

    def test15_edit_data_first_student_with_teacher(self):
        """Check is first student editing by teacher."""
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_edit_student_button()
        self.students_page.students_list.student_data. \
            enter_student_data(third_new_data_student)
        self.students_page.students_list.student_data.\
            enter_name_approved_by_custom(third_new_student.
                                          approved_by_custom)
        self.students_page.students_list.student_data. \
            click_save_data_changes_button()
        self.students_page.students_list. \
            click_exit_students_list_editor_button()
        student_with_changes = \
            data_student_for_check(third_new_data_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.main_page.get_current_url(),
                         expected_url)
        self.assertIn(student_with_changes, students_list)

    def test16_edit_cv_first_student_with_teacher(self):
        """Check is cv file added to the student's data
        by teacher."""
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_edit_student_button()
        self.students_page.students_list.student_data.add_cv(path_file_cv)
        actual_name_file = self.students_page. \
            students_list.student_data.get_name_cv_file()
        self.assertEqual(actual_name_file, expected_name_file_cv)

    def test17_edit_photo_first_student_with_teacher(self):
        """Check is photo file added to the student's data
        by teacher."""
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list.click_edit_student_button()
        self.students_page.students_list.student_data. \
            add_photo(path_file_photo)
        actual_name_file = self.students_page.students_list. \
            student_data.get_name_photo_file()
        self.assertEqual(actual_name_file, expected_name_file_photo)

    def test18_remove_first_student_with_teacher(self):
        """Check deleting first student from the student's list
        by teacher."""
        first_student = self.students_page.students_table()[0]
        self.students_page.click_edit_students_list_button()
        self.students_page.students_list. \
            click_delete_first_student_button()
        self.students_page.students_list. \
            click_exit_students_list_editor_button()
        students_list = self.students_page.students_table()
        self.assertEqual(self.main_page.get_current_url(),
                         expected_url)
        self.assertNotIn(first_student, students_list)


class TestStudentsPageFromGroupWithAdmin(unittest.TestCase):

    def setUp(self):
        """Log in by administrator, select group."""
        self.driver = webdriver.Chrome(
            executable_path=GetDriver().DRIVER_CHROME)
        self.driver.get(PathUrl().URL_SITE)
        self.driver.maximize_window()
        self.login_page = LogInPage(self.driver)
        self.login_page.auto_login(first_admin)
        self.main_page = GroupsPage(self.driver)
        self.main_page.select_group(group_name)
        self.students_page = StudentsPage(self.driver)
        return self.students_page

    def tearDown(self):
        self.driver.quit()

    def test19_opening_students_list_editor_after_selecting_group(self):
        """Check opportunity of opening student's list editor after
        selecting group and click on button 'students'."""
        self.students_page.click_students_from_group_button()
        self.students_page.click_edit_students_list_button()
        # test fail, because student's list editor does not open
        # after click on button "edit_students_list_button"
        self.assertTrue(self.students_page.students_list.
                        add_new_student_button().is_enabled())


if __name__ == '__main__':
    unittest.main()

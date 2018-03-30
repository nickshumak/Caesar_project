"""
Tests check the additional, removal and editing of
student data, adding cv_files and photo in the list of students
with different roles(administrator, coordinator, teacher)
"""

import unittest
from caesar_items.pages.students_page import StudentsPage, Student, \
    data_student_for_check
from caesar_items.pages.login_page import LogInPage
from caesar_items.pages.groups_page import GroupsPage, TopMenu
from resource.users_base import first_admin, coordinator, teacher

# main url for tests
url_for_test_start = 'http://localhost:3000/Students/Dnipro/DP-093-JS/'

# expected variables
expected_url = 'http://localhost:3000/Students/Dnipro/DP-093-JS/list'
expected_name_file_cv = 'cv.docx'
expected_name_file_photo = 'photo.jpg'
group_name = 'DP-093-JS'

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
        cls.login_page = LogInPage()
        cls.login_page.auto_login(first_admin)
        cls.main_page = GroupsPage()
        cls.main_page.top_menu.click_button_students()
        cls.main_page.select_group_students(group_name)
        cls.students_page = StudentsPage()

    @classmethod
    def tearDownClass(cls):
        StudentsPage.driver.quit()

    def tearDown(self):
        self.students_page.driver.get(url_for_test_start)
        self.students_page.driver.implicitly_wait(2)

    def test_add_new_student_with_admin(self):
        self.students_page.click_button_edit_students_list()
        self.students_page.click_button_add_new_student()
        self.students_page.enter_student_data(first_new_student)
        self.students_page.click_button_save_changes_data()
        self.students_page.click_button_exit_editor_students_list()
        student = data_student_for_check(first_new_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.students_page.get_current_url(),
                         expected_url)
        self.assertIn(student, students_list)

    def test_edit_data_first_student_with_admin(self):
        self.students_page.click_button_edit_students_list()
        self.students_page.click_button_edit_student()
        self.students_page.enter_student_data(first_new_data_student)
        self.students_page.click_button_save_changes_data()
        self.students_page.click_button_exit_editor_students_list()
        student_with_changes = \
            data_student_for_check(first_new_data_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.students_page.get_current_url(),
                         expected_url)
        self.assertIn(student_with_changes, students_list)

    def test_edit_cv_first_student_with_admin(self):
        self.students_page.click_button_edit_students_list()
        self.students_page.edit_student_with_cv(path_file_cv)
        actual_name_file = self.students_page.get_name_cv_file()
        self.assertEqual(actual_name_file, expected_name_file_cv)

    def test_edit_photo_first_student_with_admin(self):
        self.students_page.click_button_edit_students_list()
        self.students_page.edit_student_with_photo(path_file_photo)
        actual_name_file = self.students_page.get_name_photo_file()
        self.assertEqual(actual_name_file, expected_name_file_photo)

    def test_remove_first_student_with_admin(self):
        first_student = self.students_page.students_table()[0]
        self.students_page.click_button_edit_students_list()
        self.students_page.click_button_delete_first_student()
        self.students_page.click_button_exit_editor_students_list()
        students_list = self.students_page.students_table()
        self.assertEqual(self.students_page.get_current_url(),
                         expected_url)
        self.assertNotIn(first_student, students_list)


class TestStudentsPageWithCoordinator(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.login_page = LogInPage()
        cls.login_page.auto_login(coordinator)
        cls.main_page = GroupsPage()
        cls.main_page.top_menu.click_button_students()
        cls.main_page.select_group_students(group_name)
        cls.students_page = StudentsPage()

    @classmethod
    def tearDownClass(cls):
        StudentsPage.driver.quit()

    def tearDown(self):
        self.students_page.driver.get(url_for_test_start)
        self.students_page.driver.implicitly_wait(2)

    def test_add_new_student_with_coordinator(self):
        self.students_page.click_button_edit_students_list()
        self.students_page.click_button_add_new_student()
        self.students_page.enter_student_data(second_new_student)
        self.students_page.click_button_save_changes_data()
        self.students_page.click_button_exit_editor_students_list()
        student = data_student_for_check(second_new_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.students_page.get_current_url(),
                         expected_url)
        self.assertIn(student, students_list)

    def test_edit_data_first_student_with_coordinator(self):
        self.students_page.click_button_edit_students_list()
        self.students_page.click_button_edit_student()
        self.students_page.enter_student_data(second_new_data_student)
        self.students_page.click_button_save_changes_data()
        self.students_page.click_button_exit_editor_students_list()
        student_with_changes = \
            data_student_for_check(second_new_data_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.students_page.get_current_url(),
                         expected_url)
        self.assertIn(student_with_changes, students_list)

    def test_edit_cv_first_student_with_coordinator(self):
        self.students_page.click_button_edit_students_list()
        self.students_page.edit_student_with_cv(path_file_cv)
        actual_name_file = self.students_page.get_name_cv_file()
        self.assertEqual(actual_name_file, expected_name_file_cv)

    def test_edit_photo_first_student_with_coordinator(self):
        self.students_page.click_button_edit_students_list()
        self.students_page.edit_student_with_photo(path_file_photo)
        actual_name_file = self.students_page.get_name_photo_file()
        self.assertEqual(actual_name_file, expected_name_file_photo)

    def test_remove_first_student_with_coordinator(self):
        first_student = self.students_page.students_table()[0]
        self.students_page.click_button_edit_students_list()
        self.students_page.click_button_delete_first_student()
        self.students_page.click_button_exit_editor_students_list()
        students_list = self.students_page.students_table()
        self.assertEqual(self.students_page.get_current_url(),
                         expected_url)
        self.assertNotIn(first_student, students_list)


class TestStudentsPageWithTeacher(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.login_page = LogInPage()
        cls.login_page.auto_login(teacher)
        cls.main_page = GroupsPage()
        cls.main_page.top_menu.click_button_students()
        cls.main_page.select_group_students(group_name)
        cls.students_page = StudentsPage()

    @classmethod
    def tearDownClass(cls):
        StudentsPage.driver.quit()

    def tearDown(self):
        self.students_page.driver.get(url_for_test_start)
        self.students_page.driver.implicitly_wait(2)

    def test_add_new_student_with_teacher(self):
        self.students_page.click_button_edit_students_list()
        self.students_page.click_button_add_new_student()
        self.students_page.enter_student_data(third_new_student)
        self.students_page.click_button_save_changes_data()
        self.students_page.click_button_exit_editor_students_list()
        student = data_student_for_check(third_new_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.students_page.get_current_url(),
                         expected_url)
        self.assertIn(student, students_list)

    def test_edit_data_first_student_with_teacher(self):
        self.students_page.click_button_edit_students_list()
        self.students_page.click_button_edit_student()
        self.students_page.enter_student_data(third_new_data_student)
        self.students_page.click_button_save_changes_data()
        self.students_page.click_button_exit_editor_students_list()
        student_with_changes = \
            data_student_for_check(third_new_data_student)
        students_list = self.students_page.students_table()
        self.assertEqual(self.students_page.get_current_url(),
                         expected_url)
        self.assertIn(student_with_changes, students_list)

    def test_edit_cv_first_student_with_teacher(self):
        self.students_page.click_button_edit_students_list()
        self.students_page.edit_student_with_cv(path_file_cv)
        actual_name_file = self.students_page.get_name_cv_file()
        self.assertEqual(actual_name_file, expected_name_file_cv)

    def test_edit_photo_first_student_with_teacher(self):
        self.students_page.click_button_edit_students_list()
        self.students_page.edit_student_with_photo(path_file_photo)
        actual_name_file = self.students_page.get_name_photo_file()
        self.assertEqual(actual_name_file, expected_name_file_photo)

    def test_remove_first_student_with_teacher(self):
        first_student = self.students_page.students_table()[0]
        self.students_page.click_button_edit_students_list()
        self.students_page.click_button_delete_first_student()
        self.students_page.click_button_exit_editor_students_list()
        students_list = self.students_page.students_table()
        self.assertEqual(self.students_page.get_current_url(),
                         expected_url)
        self.assertNotIn(first_student, students_list)


if __name__ == '__main__':
    unittest.main()

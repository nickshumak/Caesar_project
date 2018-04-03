import os
from selenium.webdriver.support.ui import WebDriverWait
from caesar_items.pages.base_page import BasePage
from caesar_items.locators.locators import StudentsListLocators, \
    StudentLocators


class Student(object):

    def __init__(self, first_name, last_name, incoming_mark, entry_mark):
        self.first_name = first_name
        self.last_name = last_name
        self.incoming_mark = incoming_mark
        self.entry_mark = entry_mark


class StudentData(object):

    def __init__(self, driver):
        self.driver = driver

    def save_data_changes_button(self):
        """button to save changes in student data"""
        return WebDriverWait(self.driver, 10). \
            until(lambda driver: self.driver.
                  find_element(*StudentLocators.
                               SAVE_CHANGES_BUTTON))

    def click_save_data_changes_button(self):
        """click button to save changes in student data"""
        WebDriverWait(self.driver, 20). \
            until(lambda driver: self.driver.
                  find_element(*StudentLocators.
                               SAVE_CHANGES_BUTTON)).click()
        return self

    def enter_student_first_name(self, student):
        """enter student first name in window 'student data'"""
        self.driver.find_element(*StudentLocators.
                                 FIRST_NAME_TEXT_FIELD).clear()
        self.driver.find_element(*StudentLocators.
                                 FIRST_NAME_TEXT_FIELD). \
            send_keys(student.first_name)

    def enter_student_last_name(self, student):
        """enter student last name in window 'student data'"""
        self.driver.find_element(*StudentLocators.
                                 LAST_NAME_TEXT_FIELD).clear()
        self.driver.find_element(*StudentLocators.
                                 LAST_NAME_TEXT_FIELD). \
            send_keys(student.last_name)

    def select_english_level_pre_intermediate(self):
        """enter student's english level pre-intermediate in
        window 'student data'"""
        self.driver.find_element(*StudentLocators.
                                 LIST_ENGLISH_LEVEL).click()
        self.driver.find_element(*StudentLocators.
                                 PRE_INTERMEDIATE_LOW).click()

    def enter_student_mark_incoming_test(self, student):
        """enter student's mark of incoming test in
        window 'student data'"""
        self.driver.find_element(*StudentLocators.
                                 STUDENT_MARK_INCOMING_TEST). \
            clear()
        self.driver.find_element(*StudentLocators.
                                 STUDENT_MARK_INCOMING_TEST). \
            send_keys(student.incoming_mark)

    def enter_student_entry_mark(self, student):
        """enter student's entry mark in
        window 'student data'"""
        self.driver.find_element(*StudentLocators.
                                 STUDENT_ENTRY_SCORE).clear()
        self.driver.find_element(*StudentLocators.
                                 STUDENT_ENTRY_SCORE). \
            send_keys(student.entry_mark)

    def select_approved_by_varenko(self):
        """enter approved by N. Varenko in
        window 'student data'"""
        self.driver.find_element(*StudentLocators.
                                 STUDENT_APPROVED_BY).click()
        self.driver.find_element(*StudentLocators.
                                 APPROVED_BY).click()

    def enter_student_data(self, student):
        """common function for enter all necessary fields for
        student's data"""
        self.enter_student_first_name(student)
        self.enter_student_last_name(student)
        self.select_english_level_pre_intermediate()
        self.enter_student_mark_incoming_test(student)
        self.enter_student_entry_mark(student)
        self.select_approved_by_varenko()

    def add_cv(self, path_file_cv):
        """input cv file for student data"""
        self.driver.find_element(*StudentLocators.
                                 ADD_CV_BUTTON).click()
        self.driver.find_element(*StudentLocators.
                                 INPUT_PATH_CV_FILE). \
            send_keys(os.path.abspath(path_file_cv))

    def get_name_cv_file(self):
        """get name of last cv file, which is input in student data"""
        cv_names_list = []
        for cv in self.driver.find_elements(*StudentLocators.FILE_CV):
            cv_names_list.append(cv.find_element(*StudentLocators.FILE_NAME_CV).text)
        return cv_names_list[-1]

    def add_photo(self, path_file_photo):
        """input photo file for student data"""
        self.driver.find_element(*StudentLocators.
                                 ADD_PHOTO_BUTTON).click()
        self.driver.find_element(*StudentLocators.
                                 INPUT_PATH_PHOTO_FILE). \
            send_keys(os.path.abspath(path_file_photo))

    def get_name_photo_file(self):
        """get name of last photo file, which is input in student data"""
        return self.driver.find_elements(*StudentLocators.
                                         FILE_NAME_PHOTO)[-1].text

    def warnings_text_for_adding_student_with_empty_fields(self):
        """
        :return: warnings text after adding student with empty fields
        """
        warnings_text = []
        warnings = WebDriverWait(self.driver, 20). \
            until(lambda driver: self.driver.
                  find_elements(*StudentLocators.
                                WARNINGS_ADD_EMPTY_STUDENT_DATA))
        for message in warnings:
            warnings_text.append(message.text)
        return warnings_text


class StudentsList(object):

    def __init__(self, driver):
        self.driver = driver
        self.student_data = StudentData(self.driver)

    def click_delete_first_student_button(self):
        """click on button for deleting first student
        from the student's list"""
        self.driver.find_element(*StudentsListLocators.
                                 DELETE_STUDENT_BUTTON).click()
        WebDriverWait(self.driver, 20). \
            until(lambda driver: self.driver.
                  find_element(*StudentsListLocators.
                               CONFIRM_DELETING_BUTTON)).click()
        return self

    def click_add_new_student_button(self):
        """click on button for opening window for adding
        new student's data"""
        self.driver.find_element(*StudentsListLocators.
                                 ADD_NEW_STUDENT_BUTTON).click()
        return self

    def add_new_student_button(self):
        """button for opening window for adding
        new student's data"""
        return self.driver.find_element(*StudentsListLocators.
                                        ADD_NEW_STUDENT_BUTTON)

    def click_edit_student_button(self):
        """click on button for opening window for editing
        student's data"""
        self.driver.find_element(*StudentsListLocators.
                                 EDIT_STUDENT_BUTTON).click()
        return self

    def click_exit_students_list_editor_button(self):
        """click on button for exit from the student's list editor"""
        return self.driver.find_element(*StudentsListLocators.
                                        EXIT_EDIT_STUDENTS_LIST_BUTTON). \
            click()

    def click_students_list_sort_by_name_button(self):
        """click on button for sorting student's list by name"""
        WebDriverWait(self.driver, 20). \
            until(lambda driver:
                  self.driver.find_element(*StudentsListLocators.
                                           SORT_LIST_BY_NAME_BUTTON)).click()


class StudentsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.students_list = StudentsList(self.driver)

    def students_table(self):
        """
        :return: list of students data
        """
        students_data = []
        list_rows = \
            self.driver.find_elements(*StudentsListLocators.
                                      STUDENTS_LISTS_ROWS)
        for rows in list_rows:
            students_data.append(rows.text)
        return students_data

    def click_edit_students_list_button(self):
        """click on button for entering student's list editor"""
        self.driver.find_element(*StudentsListLocators.
                                 EDIT_STUDENTS_LIST_BUTTON).click()
        return self

    def click_students_from_group_button(self):
        """click on button students after selecting group"""
        WebDriverWait(self.driver, 20). \
            until(lambda driver: self.driver.
                  find_element(*StudentsListLocators.
                               STUDENTS_IN_STUDENTS_LIST_BUTTON)).click()

    def get_current_url(self):
        """page's current url"""
        return self.driver.get_url()


def data_student_for_check(student):
    """
    :param student:
    :return: student's data after adding student
    """
    data_student = [student.last_name, student.first_name,
                    'Pre-intermediate low', student.incoming_mark,
                    student.entry_mark, 'N. Varenko']
    data_student = ' '.join(data_student)
    return data_student


def remove_none_from_list(students_list):
    """
    :param students_list:
    :return: students list without None
    """
    students_list = list(filter(None, students_list))
    return students_list


def sorted_students_list(students_list):
    """
    :param students_list:
    :return: sorted students list
    """
    remove_none_from_list(students_list)
    students_list = sorted(students_list)
    return students_list

import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from caesar_items.locators.locators import \
    GroupPageLocators, LeftMenuLocators, RightMenuLocators, TopMenuLocators, \
    CreateGroupWindowLocators, LocationWindowLocators, AboutPageLocators, \
    DevelopmentPanelLocators, QualityAssurancePanelLocators, LogInLocators
from caesar_items.pages.base_page import BasePage
from caesar_items.pages.admin_page import AdminPage
from resource.url_site import PathUrl
from resource.constants_creating_group import TIME_TO_WAIT, \
    TEST_TEACHER_INDEX, TEST_FIRST_EXPERT_NAME, TEST_START_DATE


class DepartmentBaseClass(object):
    def __init__(self, driver):
        self.driver = driver

    def click_on_team_icon(self, team_icon):
        """ Click on team icon and open team panel."""
        team_icon.click()
        WebDriverWait(self.driver, TIME_TO_WAIT).until(
            EC.visibility_of_element_located(
                AboutPageLocators.PHOTO))
        return TeamPanel(self.driver)


class TeamPanel(object):
    def __init__(self, driver):
        self.driver = driver
        self.team_photos = self.driver.find_elements(*AboutPageLocators.PHOTO)
        self.teammate_name = self.driver.find_element(*AboutPageLocators.TEAMMATE_NAME).text


class DevelopmentDepartment(DepartmentBaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.team_doloto_icon = self.driver.find_element(DevelopmentPanelLocators.TEAM_DOLOTO_ICON)
        self.floppy_drive_icon = self.driver.find_element(DevelopmentPanelLocators.FLOPPY_DRIVE_TEAM_ICON)
        self.fix_machine_icon = self.driver.find_element(DevelopmentPanelLocators.FIX_MACHINE_TEAM_ICON)


class QADepartment(DepartmentBaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.light_side_team_icon = self.driver.find_element(QualityAssurancePanelLocators.LIGHT_SIDE_ICON)
        self.fluffy_dots_icon = self.driver.find_element(QualityAssurancePanelLocators.FLUFFY_DOTS_ICON)
        self.charming_chaos_icon = self.driver.find_element(QualityAssurancePanelLocators.CHARMIN_CHAOS_ICON)


class ManagementDepartment(DepartmentBaseClass):
    def __init__(self, driver):
        super().__init__(driver)


class AdditionalThanksPage(object):
    def __init__(self, driver):
        self.driver = driver


class AboutPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.development_research_button = \
            self.driver.find_element(*AboutPageLocators.
                                     DEVELOPMENT_RESEARCH_BUTTON)
        self.quality_assurance_button = \
            self.driver.find_element(*AboutPageLocators.
                                     QUALITY_ASSURANCE)
        self.management_button = \
            self.driver.find_element(*AboutPageLocators.
                                     MANAGEMENT_MENTORING_BUTTON)
        self.additional_thanks_button = \
            self.driver.find_element(*AboutPageLocators.
                                     ADDITIONAL_THANKS_BUTTON)

    def open_development_research_department(self):
        """ Get Development & Research button from about page."""
        self.development_research_button.click()
        WebDriverWait(self.driver, TIME_TO_WAIT).until(
            EC.visibility_of_element_located(
                DevelopmentPanelLocators.FIX_MACHINE_TEAM_ICON))
        return DevelopmentDepartment(self.driver)

    def open_quality_assurance_department(self):
        """ Get Quality Assurance button from about page."""
        self.quality_assurance_button.click()
        WebDriverWait(self.driver, TIME_TO_WAIT).until(
            EC.visibility_of_element_located(
                QualityAssurancePanelLocators.CHARMIN_CHAOS_ICON))
        return QADepartment(self.driver)

    def open_management_department(self):
        """ Get Management and Mentoring button from about page."""
        self.management_button.click()
        return ManagementDepartment(self.driver)

    def open_additional_thanks_page(self):
        """ Get Additional Thanks button from about page."""
        self.additional_thanks_button.click()
        return AdditionalThanksPage(self.driver)


class LocationsWindow(object):
    def __init__(self, driver):
        self.driver = driver

        self.dnipro_location = self.driver.find_element(
            *LocationWindowLocators.DNIPRO_LOCATION)

        self.chernivtsy_location = self.driver.find_element(
            *LocationWindowLocators.CHERNIVTSY_LOCATION)

        self.kyiv_location = self.driver.find_element(
            *LocationWindowLocators.KYIV_LOCATION)

        self.ivano_frankivsk_location = self.driver.find_element(
            *LocationWindowLocators.IVANO_FRANKIVSK_LOCATION)

        self.lviv_location = self.driver.find_element(
            *LocationWindowLocators.LVIV_LOCATION)

        self.rivne_location = self.driver.find_element(
            *LocationWindowLocators.RIVNE_LOCATION)

        self.sofia_location = self.driver.find_element(
            *LocationWindowLocators.SOFIA_LOCATION)

        self.save_button = self.driver.find_element(*LocationWindowLocators.SAVE_BUTTON)

        self.cancel_button = self.driver.find_element(*LocationWindowLocators.CANCEL_BUTTON)


class LeftMenu(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.create_button = self.driver.find_element(LeftMenuLocators.BUTTON_CREATE_GROUP)
        self.search_button = self.driver.find_element(*LeftMenuLocators.BUTTON_SEARCH_GROUP)
        self.edit_button = self.driver.find_element(*LeftMenuLocators.BUTTON_EDIT_GROUP)
        self.delete_button = self.driver.find_element(*LeftMenuLocators.BUTTON_DELETE_GROUP)

    def create_group_button(self):
        """ Get create button web element."""
        self.create_button.click()
        WebDriverWait(self.driver, TIME_TO_WAIT).until(
            EC.visibility_of_element_located(
                CreateGroupWindowLocators.SAVE_BUTTON))
        # return CreateGroupWindow(self.diver)

    def edit_group_button(self):
        """ Get edit button web element."""
        self.edit_button.click()
        WebDriverWait(self.driver, TIME_TO_WAIT).until(
            EC.visibility_of_element_located(
                CreateGroupWindowLocators.SAVE_BUTTON))
        # return CreateGroupWindow(self.diver)

    def delete_group_button(self):
        """ Get delete button web element."""
        self.delete_button.click()


class RightMenu(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logout_button = self.\
            driver.find_element(*RightMenuLocators.BUTTON_LOGOUT)

        self.edit_user_button = self.\
            driver.find_element(*RightMenuLocators.BUTTON_EDIT_PROFILE)

        self.user_full_name = self.\
            driver.find_element(*RightMenuLocators.USER_NAME).text

        self.user_role = self.\
            driver.find_element(*RightMenuLocators.USER_ROLE).text

    def click_logout_button(self):
        """ Click on logout web element and wait for
        Login Page."""
        self.logout_button.click()
        WebDriverWait(self.driver, TIME_TO_WAIT). \
            until(EC.visibility_of_element_located(LogInLocators.CONFIRM_ACTION))


class TopMenu(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locations_button = WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element(*TopMenuLocators.LOCATIONS_BUTTON))
        self.groups_button = WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element(*TopMenuLocators.GROUPS_BUTTON))
        self.students_button = WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element(*TopMenuLocators.STUDENTS_BUTTON))
        self.schedule_button = WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element(*TopMenuLocators.SCHEDULE_BUTTON))
        self.add_button = WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element(*TopMenuLocators.ADD_BUTTON))
        self.about_button = WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element(*TopMenuLocators.ABOUT_BUTTON))
        self.logout_button = WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element(*TopMenuLocators.BUTTON_LOGOUT))

    def click_locations_button(self):
        """ Click locations button on top menu and wait when save button appears."""
        self.locations_button.click()
        WebDriverWait(self.driver, TIME_TO_WAIT) \
            .until(EC.visibility_of_element_located(LocationWindowLocators.SAVE_BUTTON))
        return LocationsWindow(self.driver)

    def click_groups_button(self):
        """ Click groups button on top menu."""
        self.groups_button.click()
        WebDriverWait(self.driver, TIME_TO_WAIT). \
            until(EC.visibility_of_element_located(GroupPageLocators.BUTTON_MY_GROUPS))

    def click_students_button(self):
        """ Click students button on top menu."""
        self.students_button.click()
        WebDriverWait(self.driver, TIME_TO_WAIT). \
            until(EC.visibility_of_element_located(GroupPageLocators.BUTTON_ALL_GROUPS))
        return GroupsPage(self.driver)

    def click_schedule_button(self):
        """ Click schedule button on top menu."""
        self.schedule_button.click()
        WebDriverWait(self.driver, TIME_TO_WAIT). \
            until(EC.visibility_of_element_located(GroupPageLocators.BUTTON_MY_GROUPS))

    def click_add_button(self):
        """ Click add button on top menu."""
        self.add_button.click()
        WebDriverWait(self.driver, TIME_TO_WAIT). \
            until(EC.visibility_of_element_located(CreateGroupWindowLocators.SAVE_BUTTON))

    def click_about_button(self):
        """ Click about button on top menu."""
        self.about_button.click()
        WebDriverWait(self.driver, TIME_TO_WAIT). \
            until(EC.visibility_of_element_located(AboutPageLocators.DEVELOPMENT_RESEARCH_BUTTON))
        return AboutPage(self.driver)

    def click_logout_button(self):
        """ Click about button on top menu."""
        self.logout_button.click()
        WebDriverWait(self.driver, TIME_TO_WAIT). \
            until(EC.visibility_of_element_located(LogInLocators.CONFIRM_ACTION))


class GroupsPage(BasePage):
    group_page_title = 'Caesar'
    driver = None

    def __init__(self, driver):
        super().__init__(driver)
        GroupsPage.driver = driver

    def get_group_location_text(self):
        """ Get current locations from middle panel."""
        return self.driver.find_element(*GroupPageLocators.GROUP_LOCATION).text

    def my_group_button(self):
        """ Get my group web element button."""
        return self.driver.find_element(*GroupPageLocators.BUTTON_MY_GROUPS)

    def all_groups_button(self):
        """ Get all groups web element button."""
        return self.driver.find_element(*GroupPageLocators.BUTTON_ALL_GROUPS)

    def ended_groups_button(self):
        """ Get finished groups web element button."""
        return self.driver.find_element(*GroupPageLocators.ENDED_GROUPS)

    def current_groups_button(self):
        """ Get current groups web element button."""
        return self.driver.find_element(*GroupPageLocators.CURRENT_GROUPS)

    def button_boarding_groups(self):
        """ Get boarding groups web element button."""
        return self.driver.find_element(*GroupPageLocators.BOARDING_GROUPS)

    def select_group_by_name(self, group_name):
        """ Find group by name and click on it."""
        groups = self.driver.find_elements(*GroupPageLocators.GROUPS)
        for group in groups:
            if group_name == group.text:
                group.click()
                return 0
        return "group not exist"

    def list_group_current(self):
        """ Get list of groups web element from current stage."""
        groups_list = []
        groups = self.driver.find_elements(*GroupPageLocators.GROUPS)
        for group in groups:
            groups_list.append(group.text)
        return groups_list

    def list_of_groups(self):
        """ Get all groups from all stages."""
        self.ended_groups_button().click()
        list_of_groups = self.list_group_current()
        self.current_groups_button().click()
        list_of_groups += self.list_group_current()
        self.button_boarding_groups().click()
        list_of_groups += self.list_group_current()
        return list_of_groups

    def open_left_menu(self):
        """ Move mouse on left side page."""
        left_menu = self.driver.find_element(*GroupPageLocators.LEFT_MENU)
        ActionChains(self.driver). \
            move_to_element_with_offset(left_menu, 105, 300).perform()
        WebDriverWait(self.driver, TIME_TO_WAIT) \
            .until(EC.visibility_of_element_located(LeftMenuLocators.
                                                    BUTTON_SEARCH_GROUP))
        return LeftMenu(self.driver)

    def open_right_menu(self):
        """ Click on user photo."""
        self.driver.find_element(*GroupPageLocators.USER_PHOTO).click()
        WebDriverWait(self.driver, TIME_TO_WAIT). \
            until(EC.visibility_of_element_located(RightMenuLocators.
                                                   BUTTON_LOGOUT))
        return RightMenu(self.driver)

    def open_top_menu(self):
        """ Move mouse on top page."""
        top_menu = self.driver.find_element(*GroupPageLocators.TOP_MENU)
        ActionChains(self.driver).move_to_element(top_menu).perform()
        return TopMenu(self.driver)

    def open_admin_page(self):
        """ Open admin page panel."""
        self.driver.get(PathUrl().ADMIN_PAGE)
        return AdminPage(self.driver)

    def get_group_stage_text(self):
        """ Get stage text from bottom of middle panel."""
        group_stage = WebDriverWait(self.driver, TIME_TO_WAIT) \
            .until(
            EC.visibility_of_element_located(GroupPageLocators.GROUP_STAGE))
        return group_stage.text

    def confirm_deletion_button(self):
        """ Get confirm deletion web element button."""
        return self.driver. \
            find_element(*GroupPageLocators.BUTTON_CONFIRM_DELETION)

    def cancel_deletion_button(self):
        """ Get cancel deletion web element button."""
        return self.driver. \
            find_element(*GroupPageLocators.BUTTON_CANCEL_DELETION)

    def group_info_button(self):
        """ Get group's info button."""
        return self.driver.find_element(*GroupPageLocators.INFO_GROUP_BUTTON)

    def group_students_button(self):
        """ Get group's students button."""
        return self.driver.find_element(*GroupPageLocators.
                                        STUDENTS_IN_GROUP_BUTTON)

    def group_schedule_button(self):
        """ Get group's schedule button."""
        return self.driver.find_element(*GroupPageLocators.
                                        SCHEDULE_GROUP_BUTTON)

    def group_message_button(self):
        """ Get group's message button."""
        return self.driver.find_element(*GroupPageLocators.
                                        MESSAGE_GROUP_BUTTON)

    def group_edit_button(self):
        """ Get group edit button from info panel."""
        return self.driver.find_element(*GroupPageLocators.
                                        MESSAGE_GROUP_BUTTON)

    class CreateGroupWindow(object):
        def __init__(self):
            self.driver = GroupsPage.driver

        def get_group_name_field(self) -> object:
            """ Get group name field web element."""
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           GROUP_NAME_FIELD))

        def set_group_name(self, new_group_name) -> object:
            """ Set group name using entered value."""
            field_name_of_group = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           GROUP_NAME_FIELD))
            field_name_of_group.clear()
            field_name_of_group.send_keys(new_group_name)
            return self

        def clear_group_name_field(self) -> object:
            """ Clear group name field."""
            field_name_of_group = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           GROUP_NAME_FIELD))
            field_name_of_group.clear()
            return self

        def get_group_name_form(self) -> object:
            """ Get group name form web element. """
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.presence_of_element_located(CreateGroupWindowLocators.
                                               GROUP_NAME_FORM))

        def get_group_direction_form(self) -> object:
            """ Get direction form web element."""
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.presence_of_element_located(CreateGroupWindowLocators.
                                               DIRECTION_FORM))

        def get_group_location_form(self) -> object:
            """ Get location form web element."""
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.presence_of_element_located(CreateGroupWindowLocators.
                                               LOCATION_FORM))

        def get_start_date_form(self) -> object:
            """ Get start date form web element."""
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.presence_of_element_located(CreateGroupWindowLocators.
                                               START_DATE_FORM))

        def get_experts_form(self) -> object:
            """ Get expert form web element."""
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.presence_of_element_located(CreateGroupWindowLocators.
                                               EXPERTS_FORM))

        def get_value_group_name_field(self) -> str:
            """ Get value from group name field."""
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(
                    CreateGroupWindowLocators.GROUP_NAME_FIELD)). \
                get_attribute("value")

        def get_group_direction(self) -> object:
            """ Get  group direction web element."""
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           DIRECTION_DROP_LIST))

        def set_group_direction(self, str_direction) -> object:
            """ Set  chosen group direction."""
            list_direction = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           DIRECTION_DROP_LIST))
            select_direction = Select(list_direction)
            select_direction.select_by_index(str_direction)
            return self

        def get_value_of_direction(self) -> str:
            """ Get value of group from direction field."""
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(
                    CreateGroupWindowLocators.DIRECTION_DROP_LIST)). \
                get_attribute("value")

        def get_group_location(self) -> object:
            """ Get  group location web element."""
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           LOCATION_DROP_LIST))

        def set_group_location(self, location_index) -> object:
            """ Set  chosen group location."""
            locations_get = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           LOCATION_DROP_LIST))
            locations_get.click()
            select_location = Select(locations_get)
            select_location.select_by_index(location_index)
            return self

        def get_value_of_location(self) -> str:
            """ Get value from group location field."""
            drop_list_location_of_group = WebDriverWait(self.driver,
                                                        TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           LOCATION_DROP_LIST))
            location_of_group = drop_list_location_of_group. \
                get_attribute("value")
            return location_of_group

        def get_teacher_add_button(self) -> object:
            """ Get  teacher add button web element."""
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           ONE_MORE_TEACHER_BUTTON))

        def get_teachers_drop_list(self) -> object:
            """ Get  teachers drop down list web element ."""
            button_add_teacher = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           ONE_MORE_TEACHER_BUTTON))
            button_add_teacher.click()
            drop_list_teachers = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           TEACHERS_DROP_LIST))
            return drop_list_teachers

        def select_teacher(self, teacher_name) -> object:
            """ Select teacher from teachers drop down list."""
            button_add_teacher = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           ONE_MORE_TEACHER_BUTTON))
            button_add_teacher.click()
            drop_list_teachers = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           TEACHERS_DROP_LIST))
            drop_list_teachers.click()
            select = Select(drop_list_teachers)
            select.select_by_index(teacher_name)
            self.driver.find_element(CreateGroupWindowLocators.
                                     ACCEPT_TEACHER_BUTTON).click()
            return self

        def add_teacher(self) -> object:
            """ Accept choosing teacher from teachers drop down list."""
            button_add_teacher = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           ONE_MORE_TEACHER_BUTTON))
            button_add_teacher.click()
            WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           ACCEPT_TEACHER_BUTTON)).click()
            return self

        def get_values_from_added_teachers_list(self) -> list:
            """ Get values from "added teachers" list."""
            added_teachers_form = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.presence_of_element_located(CreateGroupWindowLocators.
                                               ADDED_TEACHERS_FORM))
            added_teachers_list = added_teachers_form.\
                find_elements(By.CLASS_NAME, 'list-item')
            list_of_teachers_values = []
            for added_teacher in added_teachers_list:
                list_of_teachers_values.append(added_teacher.text)
            return list_of_teachers_values

        def set_start_date(self, start_date_value) -> object:
            """ Set value to "start date" field."""
            field_date_start_field = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           START_DATE_FIELD))
            field_date_start_field.send_keys(start_date_value)
            field_date_finish = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           FINISH_DATE_FIELD))
            field_date_finish.send_keys(Keys.ENTER)
            return self

        def submit_group_creating_button(self) -> object:
            """ End group creating and save all fields."""
            button_save_group = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           SAVE_BUTTON))
            button_save_group.click()
            return self

        def get_save_group_button(self) -> object:
            """ Get "Save" button web element."""
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           SAVE_BUTTON))

        def get_warning_message_by_form(self, form) -> object:
            """ Get  pop-up warning message web element, attached to this form."""
            warning_message = None
            hints = form.find_elements(By.CLASS_NAME, 'hint')
            for hint in hints:
                hint = hint.find_elements(
                    By.TAG_NAME, 'p')
                for message_text in hint:
                    warning_message = message_text.text
            return warning_message

        def cancel_button_get(self) -> object:
            """ Get "Cancel" button web element."""
            return WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           CANCEL_BUTTON))

        def add_expert(self, expert_name) -> object:
            """ Add expert - first click the "+one more expert" button, then set
            expert's name and then click  "accept  expert" button."""
            WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(
                    CreateGroupWindowLocators.ADD_EXPERT_BUTTON)).click()
            WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(
                    CreateGroupWindowLocators.EXPERTS_NAME_FIELD)). \
                send_keys(expert_name)
            WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(
                    CreateGroupWindowLocators.ACCEPT_EXPERT_BUTTON)).click()
            return self

        def get_added_experts_list(self) -> list:
            """ Get values from "added experts" list."""
            added_experts_form = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.presence_of_element_located(CreateGroupWindowLocators.
                                               ADDED_EXPERTS_LIST))
            added_experts_list = added_experts_form.\
                find_elements(By.CLASS_NAME, 'list-item')
            list_of_values = []
            for added_expert in added_experts_list:
                list_of_values.append(added_expert.text)
            return list_of_values

        def auto_fill_all_fields(self, new_group_name, location):
            """ Fill  all fields, to create some group,
                            function used to test deleting of groups."""
            if location == "Chernivtsy":
                location_index = 0
            elif location == "Dnipro":
                location_index = 1
            elif location == "Ivano-Frankivsk":
                location_index = 2
            elif location == "Kyiv":
                location_index = 3
            elif location == "Lviv":
                location_index = 4
            elif location == "Rivne":
                location_index = 5
            elif location == "Sofia":
                location_index = 6
            else:
                location_index = 1
            direction_field = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           DIRECTION_DROP_LIST))
            direction_field.click()
            directions_list = direction_field.find_elements(
                By.TAG_NAME, 'option')
            random_direction_index = random.randint(
                1, 3)
            select_direction = Select(direction_field)
            select_direction.select_by_index(random_direction_index)
            location_field = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           LOCATION_DROP_LIST))
            location_field.click()
            random_location_index = location_index
            select_location = Select(location_field)
            select_location.select_by_index(random_location_index)
            button_add_teacher = WebDriverWait(self.driver, TIME_TO_WAIT). \
                until(EC.element_to_be_clickable(CreateGroupWindowLocators.
                                                 ONE_MORE_TEACHER_BUTTON))
            button_add_teacher.click()
            drop_list_teachers = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           TEACHERS_DROP_LIST))
            drop_list_teachers.click()
            select = Select(drop_list_teachers)
            select.select_by_index(TEST_TEACHER_INDEX)
            WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           ACCEPT_TEACHER_BUTTON)).click()
            WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           ADD_EXPERT_BUTTON)).click()
            WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(
                    CreateGroupWindowLocators.EXPERTS_NAME_FIELD)).send_keys(
                TEST_FIRST_EXPERT_NAME)
            WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           ACCEPT_EXPERT_BUTTON)).click()
            field_date_start_field = WebDriverWait(self.driver,
                                                   TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           START_DATE_FIELD))
            field_date_start_field.send_keys(TEST_START_DATE)
            field_date_finish = WebDriverWait(self.driver, TIME_TO_WAIT).until(
                EC.element_to_be_clickable(CreateGroupWindowLocators.
                                           FINISH_DATE_FIELD))
            field_date_finish.send_keys(Keys.ENTER)

            self.set_group_name(new_group_name)
            self.submit_group_creating_button()

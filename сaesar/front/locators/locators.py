from selenium.webdriver.common.by import By


class LogInLocators(object):
    LOGIN_FIELD = (By.NAME, 'login')
    PASSWORD_FIELD = (By.NAME, 'password')
    CONFIRM_ACTION = (By.CLASS_NAME, 'submit')
    FIELD_MESSAGE = (By.CLASS_NAME, 'message')


class GroupPageLocators(object):
    GROUP_LOCATION = (By.CLASS_NAME, 'groupLocation')
    BUTTON_SEARCH = (By.CSS_SELECTOR, 'div.search')

    # GROUPS = (By.CLASS_NAME, 'group-collection row')

    BUTTON_MY_GROUPS = (By.CLASS_NAME, 'myGroups')
    BUTTON_ALL_GROUPS = (By.CLASS_NAME, 'allGroups')
    BUTTONS_STAGE_GROUPS = (By.CLASS_NAME, 'stage-toggle')

    # надо определиться как делаем, так не красиво или через массив?селекторы проверила
    ENDED_GROUPS = (By.CSS_SELECTOR, '.stage-toggle > label:nth-child(2)')
    CURRENT_GROUPS = (By.CSS_SELECTOR, '.stage-toggle > label:nth-child(4)')
    FUTURE_GROUPS = (By.CSS_SELECTOR, '.stage-toggle > label:nth-child(6)')

    GROUPS = (By.CLASS_NAME, 'small-group-view')

    # main section
    GROUP_NAME = (By.CLASS_NAME, 'content-header-group-name')
    BUTTON_EDIT_GROUP = (By.NAME, 'edit')
    BUTTON_INFO_GROUP = (By.NAME, 'info')
    BUTTON_STUDENTS_IN_GROUP = (By.NAME, 'students')
    BUTTON_SCHEDULE_GROUP = (By.NAME, 'shedule')
    BUTTON_MESSAGE_GROUP = (By.NAME, 'message')

    GROUP_COORDINATION = (By.CLASS_NAME, 'group_coordination')
    GROUP_INFO = (By.CLASS_NAME, 'group_info')
    KEY_DATES = (By.CLASS_NAME, 'key - dates')
    GROUP_STAGE_TITLE = (By.CLASS_NAME, 'groupStageTitle')
    GROUP_STAGE = (By.CLASS_NAME, 'groupStage')

    LEFT_MENU = (By.CSS_SELECTOR, '#left-menu > div')
    USER_PHOTO = (By.CLASS_NAME, 'user-photo')
    TOP_MENU = (By.CLASS_NAME, 'row')


class RightMenuLocators(object):
    BUTTON_EDIT_PROFILE = (By.CLASS_NAME, 'btn-edit')
    USER_NAME = (By.CLASS_NAME, 'name')
    USER_ROLE = (By.CLASS_NAME, 'role')
    BUTTON_LOGOUT = (By.CSS_SELECTOR, 'a.logout:nth-child(3)')


class LeftMenuLocators(object):
    BUTTON_CREATE_GROUP = (By.XPATH, '//*[@title = "Create"]')
    BUTTON_SEARCH_GROUP = (By.XPATH, '//*[@title = "Search"]')
    BUTTON_EDIT_GROUP = (By.XPATH, '//*[@title = "Edit"]')
    BUTTON_DELETE_GROUP = (By.XPATH, '//*[@title = "Delete"]')


class TopMenuLocators(object):
    BUTTON_LOCATIONS = (By.CSS_SELECTOR, 'div.itemMenu:nth-child(1)')
    BUTTON_GROUPS = (By.CSS_SELECTOR, 'div.itemMenu:nth-child(2)')
    BUTTON_STUDENTS = (By.CSS_SELECTOR, 'div.itemMenu:nth-child(3)')
    BUTTON_SCHEDULE = (By.CSS_SELECTOR, 'div.itemMenu:nth-child(4)')
    BUTTON_ADD = (By.CSS_SELECTOR, 'div.itemMenu:nth-child(5)')
    BUTTON_ABOUT = (By.CSS_SELECTOR, 'div.itemMenu:nth-child(6)')

    BUTTON_LOGOUT = (By.CLASS_NAME, 'logout')


class AdminPageLocators(object):
    ADD_USER = (By.XPATH, ".//*[text()='Add user']")
    ADD_GROUP = (By.XPATH, "/.//*[text()='Add group']")
    ADD_STUDENT = (By.XPATH, ".//*[text()='Add student']")
    TAB_USERS = (By.CSS_SELECTOR, "a[href*='users']")
    TAB_GROUPS = (By.CSS_SELECTOR, "a[href*='groups']")
    TAB_STUDENTS = (By.CSS_SELECTOR, "a[href*='students']")
    BUTTON_ESCAPE = (By.CSS_SELECTOR, '.btn.btn-warning.home')
    TITLE_ENTITY = (By.CSS_SELECTOR, '.modal-title')
    MAIN_TABLE = (By.XPATH, ".//*[@id='students']/div/table/tbody//td[position()<last()]")


class CreateEditUsersLocators(object):
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    ROLE = (By.NAME, "role")
    LOCATION = (By.NAME, "location")
    PHOTO = (By.NAME, "photo")
    LOGIN_FIELD = (By.NAME, "login")
    PASSWORD_FIELD = (By.NAME, "password")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, ".btn.btn-primary.submit")


class CreateEditGroupsLocators(object):
    NAME = (By.NAME, "name")
    LOCATION = (By.NAME, "location")
    DIRECTION = (By.NAME, "direction")
    START_DATE = (By.NAME, "startDate")
    FINISH_DATE = (By.NAME, "finishDate")
    TEACHERS = (By.NAME, "teachers")
    EXPERTS = (By.NAME, "experts")
    STAGE = (By.NAME, "stage")
    BUDGET = (By.NAME, "budgetOwner")
    BUTTON_SUBMIT = (By.CSS_SELECTOR, ".btn.btn-primary.submit")


class CreateEditStudentsLocators(object):
    GROUP_ID = (By.NAME, 'groupID')
    NAME = (By.NAME, "name")
    LAST_NAME = (By.NAME, "lastName")
    ENGLISH_LEVEL = (By.NAME, "englishLevel")
    CV_URL = (By.NAME, "CvUrl")
    IMAGE = (By.NAME, "imageUrl")
    ENTRY_SCORE = (By.NAME, "entryScore")
    APPROVED_BY = (By.NAME, 'approvedBy')
    BUTTON_SUBMIT = (By.CSS_SELECTOR, ".btn.btn-primary.submit")

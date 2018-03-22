from selenium.webdriver.common.by import By


class LogInLocators(object):
    LOGIN_FIELD = (By.NAME, 'login')
    PASSWORD_FIELD = (By.NAME, 'password')
    TEXT_FIELD = (By.CLASS_NAME, 'message')
    CONFIRM_ACTION = (By.ID, "")
    FIELD_MESSAGE = (By.CLASS_NAME, "message")


class GroupPageLocators(object):
    GROUP_LOCATION = (By.CLASS_NAME, 'groupLocation')
    BUTTON_SEARCH = (By.CSS_SELECTOR, 'div.search')
    GROUPS = (By.CLASS_NAME, 'group-collection row')
    BUTTON_MY_GROUPS = (By.CLASS_NAME, 'myGroups')
    BUTTON_ALL_GROUPS = (By.CLASS_NAME, 'allGroups')
    BUTTONS_STAGE_GROUPS = (By.CLASS_NAME, 'stage-toggle')

    # надо определиться как делаем, так не красиво или через массив?селекторы проверила
    ENDED_GROUPS = (By.CSS_SELECTOR, '.stage-toggle > label:nth-child(2)')
    CURRENT_GROUPS = (By.CSS_SELECTOR, '.stage-toggle > label:nth-child(4)')
    FUTURE_GROUPS = (By.CSS_SELECTOR, '.stage-toggle > label:nth-child(6)')

    GROUPS = (By.CLASS_NAME, 'small-group-view col-md-6')

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


class RightBarLocators(object):
    BUTTON_EDIT_PROFILE = (By.CLASS_NAME, 'btn-edit')
    USER_NAME = (By.CLASS_NAME, 'name')
    USER_ROLE = (By.CLASS_NAME, 'role')
    BUTTON_LOGOUT = (By.CLASS_NAME, 'logout')


class LeftBarLocators(object):
    BUTTON_CREATE_GROUP = (By.XPATH, '//*[@title = "Create"]')
    BUTTON_SEARCH_GROUP = (By.XPATH, '//*[@title = "Search"]')
    BUTTON_EDIT_GROUP = (By.XPATH, '//*[@title = "Edit"]')
    BUTTON_DELETE_GROUP = (By.XPATH, '//*[@title = "Delete"]')


class HeaderBarLocators(object):
    LIST_BUTTONS_HEADER_BAR = (By.CLASS_NAME, 'containerMainMenu')

    # опять таки массив или так?
    BUTTON_LOCATIONS = (By.CSS_SELECTOR, 'div.itemMenu: nth - child(1)')
    BUTTON_GROUPS = (By.CSS_SELECTOR, 'div.itemMenu:nth-child(2)')
    BUTTON_STUDENTS = (By.CSS_SELECTOR, 'div.itemMenu:nth-child(3)')
    BUTTON_SCHEDULE = (By.CSS_SELECTOR, 'div.itemMenu:nth-child(4)')
    BUTTON_ADD = (By.CSS_SELECTOR, 'div.itemMenu:nth-child(5)')
    BUTTON_ABOUT = (By.CSS_SELECTOR, 'div.itemMenu:nth-child(6)')

    BUTTON_LOGOUT = (By.CLASS_NAME, 'logout')

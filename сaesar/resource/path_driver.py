import os


class GetDriver(object):
    DRIVER_CHROME = os.path.dirname(__file__) + '/chromedriver.exe'
    DRIVER_FIREFOX = os.path.dirname(__file__) + '/geckodriver.exe'

import os


class GetDriver(object):
    CHROME_DRIVER = os.path.dirname(__file__) + '/chromedriver.exe'
    FIREFOX_DRIVER = os.path.dirname(__file__) + '/geckodriver.exe'

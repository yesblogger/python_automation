from selenium import webdriver


class webDriver:

    def __init__(self):
        """[initializing the instance with the chrome driver]
        """
        # setting the chrome driver
        self.driver = webdriver.Chrome()
        # implicitly wait for 30 seconds for the DOM to load when searching for an element
        self.driver.implicitly_wait(30)

    def closeConnection(self):
        """[Method closes the chrome driver when called]
        """
        self.driver.quit()

    def setInitialURL(self):
        self.driver.get('https://www.freshworks.com/company/partners/find-partners/')

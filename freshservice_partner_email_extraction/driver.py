from selenium import webdriver
import time


class webDriver:

    def __init__(self, country):
        """[initializing the instance with the chrome driver]
        """
        # setting the country attribute
        self.country = country
        # setting the chrome driver
        self.driver = webdriver.Chrome()
        # implicitly wait for 30 seconds for the DOM to load when searching for an element
        self.driver.implicitly_wait(30)

    def closeConnection(self):
        """[Method closes the chrome driver when called]
        """
        self.driver.quit()

    def setInitialURL(self):
        """[Set the URL of the partner portal in the driver]
        """
        self.driver.get('https://www.freshworks.com/company/partners/find-partners/')
        time.sleep(3)

    def setFilter(self):
        """[Find the filter element and set the filter]
        """
        pass
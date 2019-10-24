#driver.execute_script("arguments[0].setAttribute('class','vote-link up voted')", element)
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
        self.driver.get(
            'https://www.freshworks.com/company/partners/find-partners/')
        time.sleep(3)

    def setFilter(self):
        """[Find the filter elements and set the filter criteria]
        """
        try:
            # fetching the input element where country is entered
            countryInputElement = self.driver.find_element_by_xpath(
                '//input[@id="partner_country_input"]')
            # updating the value attribute of the input field using javascript
            self.driver.execute_script(
                f"arguments[0].setAttribute('value',{self.country})", countryInputElement)
            # fetching label elements containing the checkboxes for Partner Type
            labelElements = self.driver.find_elements_by_xpath(
                '//div[./h6/text()="Partner Type"]/label')
            # pausing the thread for 2 secods
            time.sleep(2)
            # looping over the label elements and clicking them
            for i in labelElements:
                i.click()
                time.sleep(2)
        except Exception as error:
            print(error)
            self.driver.quit()

    def captureData(self, writer):
        """[Capture name and email and put it into a csv file]

        Arguments:
            writer {[csv object]} -- [file object]
        """
        try:
            # //div[@data-country="IN"]//div[@class="reseller-info"]

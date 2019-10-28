from selenium import webdriver
import time

#driver.execute_script("arguments[0].setAttribute('class','vote-link up voted')", element)


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

    def captureData(self, writer, countryCode):
        """[Capture name and email and put it into a csv file]

        Arguments:
            writer {[csv object]} -- [file object]
        """
        try:
            # xpath for filtering primany block
            primaryBlock = self.driver.find_elements_by_xpath(
                f'//div[@data-country="{countryCode}"]//div[@class="reseller-info"]')
            # pausing the thread for 2 seconds
            time.sleep(2)
            # iterating over the primaryBlock elements and fetching the name and email
            for elem in primaryBlock:
                # extracting key data points
                name = elem.find_element_by_xpath(
                    './h6').get_attribute('textContent')
                email = elem.find_element_by_xpath(
                    './span/a').get_attribute('textContent')
                # writing data points into the file
                writer.writerow({'Name': name, 'Email': email})
            # pausing the thread for 2 seconds
            time.sleep(2)
            # scrolling the page
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        except Exception as error:
            print(error)
            self.driver.quit()

    def captureAllData(self, writer):
        """[Capture all emails on the website irrespective of the country]

        Arguments:
            writer {[CSV dictwriter object]} -- [file object]
        """
        try:
            # capturing the primary block
            primaryBlock = self.driver.find_elements_by_xpath(
                '//div[@class="reseller-info"]')
            # pausing the thread for 2 seconds
            time.sleep(2)
            # iterating over the primaryblock to capture name and email
            for elem in primaryBlock:
                # extracting key data points
                name = elem.find_element_by_xpath(
                    './h6').get_attribute('textContent')
                email = elem.find_element_by_xpath(
                    './span/a').get_attribute('textContent')
                # writing data points into the file
                writer.writerow({'Name': name, 'Email': email})
            # pausing the thread for 2 seconds
            time.sleep(2)
            # scrolling the page
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        except Exception as error:
            print(error)
            self.driver.quit()

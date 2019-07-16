"""Given a domain, this class will find the company name from the official website
"""
from selenium import webdriver


class Search():
    """This class will create a driver that visits the official website of a domain and 
       fetched the name from the title.
    """

    def __init__(self):
        """Initiating the class
        """
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(10)

    def find_name(self, domain):
        """Given a domain name, it opens the official website and gets the title content

        Arguments:
            domain {string} -- [domain with or without www]
        """
        # get company information from a valid domain
        self.browser.get(f"https://{domain}")
        title = self.browser.title if self.browser.title != None else "No Company Info"

        return title

    def close_connection(self):
        """close the open connection
        """
        self.browser.quit()

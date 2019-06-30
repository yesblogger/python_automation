"""Create instance of chrome webdriver; find search duckduckgo and find domain from a sub-domain.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import re


class Driver():

    def __init__(self):
        """Initiating the class by creating a chrome driver
        """
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 10)

    def find_domain(self, sub):
        """Search and fetch domain

        Arguments:
            sub {string} -- [complete domain name of the company]
        """

        # Filter the sub-domain
        sub = Driver.filter_sub(sub)

        # Go to duckduck go page and search for the sub
        self.browser.get(f"https://duckduckgo.com/?q={sub}&t=h_&ia=web")

        # fetch all relevent elements from the page
        elements = self.wait.until(ec.presence_of_all_elements_located(
            (By.XPATH, "//div[@class='result results_links_deep highlight_d result--url-above-snippet']")))

        # pass elements to a static function where relevent domain is filtered
        domain = Driver.filter_domains(elements, sub)

        # return the filtered domain
        return domain

    def close_connection(self):
        """Closes the connection of the web driver
        """
        self.browser.quit()

    @staticmethod
    def filter_sub(s_domain):
        """Converts sub-domain into domain initials

        Arguments:
            s_domain {String} -- [sub-domain as string]
        """
        return s_domain.split(".")[0]

    @staticmethod
    def filter_domains(e, sub):
        """Filter relevent element from a list of elements

        Arguments:
            e {selenium element objects} -- [multiple element objects]
            sub {string} -- [partial domain name]
        """

        for i in e:
            # fetch domain attribute
            try:
                domain = i.get_attribute("data-domain")
                # Filtering the data-domain string
                n_domain = re.match(r"(www)?(\.)?([a-z0-9-]+)(\.\w+)", domain)
                if n_domain is not None:
                    n_domain = n_domain.group(3)
                else:
                    n_domain = ""
            except:
                n_domain = ""
            # check sub is in fetched data
            if sub in n_domain and len(sub) == len(n_domain):
                return domain

        return "Domain not found"

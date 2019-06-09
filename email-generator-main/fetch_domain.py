# -*- coding: utf-8 -*-
"""
Created on Wed May 29 21:22:30 2019

@author: Flotomate Amartya
"""

import clearbit
import lxml.html
from selenium import webdriver


class Domain():
    """
    Enter the key and domain name in string
    """

    def __init__(self, key):
        self.key = key

    def get_domain(self, company_name):
        # authenticating clearbit with the key
        clearbit.key = self.key
        # using the company name we will now return the domain name
        try:
            name = clearbit.NameToDomain.find(name=company_name)['domain']
        except:
            name = None
        # check if name is none, if yes then do a google search
        if name == None:
            # now we will get the domain from the web
            # generating the url for the search
            n_name = "+".join(company_name.split(" "))
            # creating a web driver to make a search
            driver = webdriver.Chrome()
            # open brower with the url
            driver.get(f'https://duckduckgo.com/?q={n_name}&t=h_&ia=web')
            # executing javascript to fetch the html of the search page
            response = driver.execute_script(
                'return document.documentElement.outerHTML')
            # create a lxml object fetch the element
            extractor = lxml.html.fromstring(response)
            # fecth domain name using xpath
            try:
                name = extractor.xpath('//div[@id="r1-0"]/@data-domain')[0]
            except:
                driver.quit()
                return "No Domain Found"
            # close the driver
            driver.quit()

        # returing the final domain name
        return str(name)

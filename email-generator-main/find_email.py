# -*- coding: utf-8 -*-
"""
Created on Sun May 12 22:23:45 2019

@author: Amartya
"""

from pyhunter import PyHunter

class Email():
    
    def __init__(self, key):
        self.key = key
    
    def find_email(self, name, d_name):
        # creating a hunter object
        hunter = PyHunter(self.key)
    
        #proper capitalization of the name
        name = " ".join([i.capitalize() for i in name.split(" ")])
    
        #calling api to fetch email and confidency score
        try:
            email, c_score = hunter.email_finder(domain=d_name, full_name=name)
            #rasing exception when non type in returned
            if email == None:
                raise ValueError
        except BaseException:
            email, c_score = ('NotFound', 0)
            
        return email, c_score
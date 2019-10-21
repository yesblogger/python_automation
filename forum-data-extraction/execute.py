

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 16:23:44 2019

@author: Amartya Gupta
"""

import requests
import lxml.html
import csv
import time

def main():
    #ask for the number of pages to be fetched from the user
    pages = int(input("Please enter the number of pages that you want to fetch: "))
    #creating url variable
    url = "https://support.freshservice.com/support/discussions/forums/289922/page/{page}?url_locale="
    #url section for input completion
    url_c = "https://support.freshservice.com"
    #field counter
    counter = 1
    #open a csv file to write all data
    with open("forum_data.csv", "w", newline='') as o_file:
        #creating a header
        header = ['Sr','Title', 'Url']
        #creating writer object
        writer = csv.DictWriter(o_file, fieldnames=header)
        #write the header
        writer.writeheader() 
        
        # creating range and iterating over the pages
        for p in range(1,pages):
            #sleep for three seconds
            time.sleep(2)
            #fetch one page at a time
            source = requests.get(url.format(page=p)).text
            #create parse object
            parse = lxml.html.fromstring(source)
            #parse source using xpath
            items = parse.xpath('//a[@class="c-link"]')
            #iteration over items and write in csv file
            for item in items:
                writer.writerow({'Sr': counter, 'Title': item.attrib['title'], 'Url': url_c + item.attrib['href']})
                counter += 1
                
                
if __name__ == "__main__":
    main()
    



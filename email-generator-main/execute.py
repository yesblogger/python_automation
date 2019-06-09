# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 23:03:48 2019

@author: Amartya
"""

import csv
from fetch_domain import Domain
from find_email import Email


def main():
    # get file name of the source file
    s_file = input('File name or path: ')
    d_key = input('Enter Clearbit key: ')
    h_key = input('Enter hunter key: ')
    
    #open file then iterate over the rows
    with open(s_file, 'r') as i_file:
        #create a csv object
        i_cursor = csv.reader(i_file)
        #omitting the header value row
        next(i_cursor)
        
        #setting up custom classes
        domain = Domain(d_key)
        email = Email(h_key)
        
        #opeing the output file
        with open('output_data.csv', 'w', newline='') as o_file:
            #creatng the header for the new file
            fieldnames = ['Name', 'Company Domain', 'Email', 'Score']
            # creating the csv object
            o_cursor = csv.DictWriter(o_file, fieldnames=fieldnames)
            #wring the header of the file
            o_cursor.writeheader()
            #looping over rows to fetch the values
            for in_val in i_cursor:
                # fetching the name and the comapany name
                name, company_name = in_val[0], in_val[1]
                #getting the domain
                d_name = domain.get_domain(company_name)
                #get email using domain
                c_email, a_score = email.find_email(name, d_name)
                #wrting data in the output file
                o_cursor.writerow({'Name': name, 'Company Domain': d_name, 'Email': c_email, 'Score': a_score})
                
    # closing the function            
    return None
            
    
if __name__ == "__main__":
    main()
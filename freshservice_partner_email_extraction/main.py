# extract name and email
# input country name
# input file name
# driver open browser
# set initial url path
# driver set filter
# open csv file
# driver extract name and email element
# write name and email in the csv file

import csv
from driver import webDriver

country_list = ['India', 'Afghanistan', 'Argentina', 'Australia', 'Austria', 'Belarus', 'Belgium', 'Brazil', 'Canada', 'Chile', 'China', 'Colombia', 'Costa Rica', 'Czech Republic', 'Dominican Republic', 'Finland',
                'France', 'Germany', 'Hong Kong', 'Iceland', 'India', 'Indonesia', 'Ireland', 'Italy', 'Jamaica', 'Japan', 'Korea (Republic of)', 'Kuwait', 'Malaysia', 'Mexico', 'Netherlands', 'Norway', 'Pakistan',
                'Panama', 'Peru', 'Philippines', 'Poland', 'Puerto Rico', 'Russian Federation', 'Rwanda', 'Saudi Arabia', 'Singapore', 'South Africa', 'Spain', 'Sweden', 'Switzerland', 'Taiwan, Province of China',
                'Thailand', 'Trinidad and Tobago', 'Turkey', 'Ukraine', 'United Arab Emirates', 'United Kingdom of Great Britain and Northern Ireland', 'United States of America', 'Vietnam']

if __name__ == '__main__':
    # initiating the main script
    while True:
        # ask for a valid country name.
        country = input('Please enter a country name: ')
        if country in country_list:
            break
    # ask for a filename
    filename = input('Please enter a filename: ')

    # create instance of the driver
    browser = webDriver(country)
    # set initial URL in the driver. Freshservice partner search page will open
    browser.setInitialURL()
    # In the partner search page, we will set the filter with the counter info
    browser.setFilter()
    # now we will open a csv file and capture the name and email details
    with open(f'{filename}.csv', mode='w', newline='') as w_file:
        # definging the heading of the file
        heading = ['Name', 'Email']
        # creating a csv writer object
        writer = csv.DictWriter(w_file, fieldnames=heading)
        # writing the first row
        writer.writeheader()
        # now we are going to pass on the writer object to the capture function
        browser.captureData(writer)
    # once the fetching of the data is done we will close the browser
    browser.closeConnection()

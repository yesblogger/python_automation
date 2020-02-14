from automate import webDriver
import csv

country_list = {'India': 'IN', 'Afghanistan': 'AF', 'Argentina': 'AR', 'Australia': 'AU', 'Austria': 'AT', 'Belarus': 'BY', 'Belgium': 'BE', 'Brazil': 'BR', 'Canada': 'CA', 'Chile': 'CL', 'China': 'CN', 'Colombia': 'CO', 'Costa Rica': 'CR  ', 'Czech Republic': 'CZ', 'Dominican Republic': 'DO', 'Finland': 'FI',
                'France': 'FR', 'Germany': 'DE', 'Hong Kong': 'HK', 'Iceland': 'IS', 'Indonesia': 'ID', 'Ireland': 'IE', 'Italy': 'IT', 'Jamaica': 'JM', 'Japan': 'JP', 'Korea (Republic of)': 'KR', 'Kuwait': 'KW', 'Malaysia': 'MY', 'Mexico': 'MX', 'Netherlands': '', 'Norway': '', 'Pakistan': '',
                'Panama': '', 'Peru': '', 'Philippines': '', 'Poland': '', 'Puerto Rico': '', 'Russian Federation': '', 'Rwanda': '', 'Saudi Arabia': '', 'Singapore': '', 'South Africa': '', 'Spain': '', 'Sweden': '', 'Switzerland': '', 'Taiwan, Province of China': '',
                'Thailand': '', 'Trinidad and Tobago': '', 'Turkey': '', 'Ukraine': '', 'United Arab Emirates': '', 'United Kingdom of Great Britain and Northern Ireland': '', 'United States of America': 'US', 'Vietnam': '', 'All': ''}

if __name__ == '__main__':
    # initiating the main script
    while True:
        # ask for a valid country name.
        country = input('Please enter a country name: ')
        if country in country_list.keys():
            break
    # ask for a filename
    filename = input('Please enter a filename: ')

    # create instance of the driver
    browser = webDriver(country)
    # set initial URL in the driver. Freshservice partner search page will open
    browser.setInitialURL()
    # In the partner search page, we will set the filter with the counter info
    # browser.setFilter()
    # now we will open a csv file and capture the name and email details
    with open(rf"output\{filename}.csv", mode='w', newline='', encoding="utf-8") as w_file:
        # definging the heading of the file
        heading = ['Name', 'Email']
        # creating a csv writer object
        writer = csv.DictWriter(w_file, fieldnames=heading)
        # writing the first row
        writer.writeheader()
        # now we are going to pass on the writer object to the capture function
        if country != 'All':
            browser.captureData(writer, country_list[country])
        else:
            browser.captureAllData(writer)
    # once the fetching of the data is done we will close the browser
    browser.closeConnection()

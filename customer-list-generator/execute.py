"""Main function to convert a list of sub-domains into a csv file with Company Name, 
URL.
"""
import csv
import os.path
from find_domain import Driver
from find_company import Search
import secrets
import time


def main():
    # ask the directory path
    #direct = input("Please enter the directory path of the input folder: ")
    # ask the user for the file name
    in_file = input("Please enter the file name: ")
    # ask how many files are there
    file_no = int(input("How many files are there: "))

    # creating a list of time for generating domain
    times = [1, 2, 3]

    # Create connections to the driver
    domain_driver = Driver()
    company_driver = Search()

    # initiate loop to open file one at a time and read data
    for i in range(1, file_no + 1):
        # open file one at a time
        with open(f"{in_file}-({i}).csv", mode="r") as i_file:
            # creating a reader object to read the opened file
            reader = csv.reader(i_file)
            # skipping the header section
            next(reader)
            # now checking whether output file exists or not. Based on that initate two types of write
            if not os.path.exists("output.csv"):
                # file doesn't exists create a new file and write
                with open("output.csv", mode="w", newline="") as o_file:
                    # create the header for the new file
                    header = ["Domain", "Company Details"]
                    # creating a writer object with the header
                    writer = csv.DictWriter(o_file, fieldnames=header)
                    # write the header first
                    writer.writeheader()
                    # iterate over the input file and write the rows
                    for i in reader:
                        try:
                            # random sleep
                            time.sleep(secrets.choice(times))
                            # first generate the domain name
                            domain = domain_driver.find_domain(i[0])
                            if domain != "Domain not found":
                                # generate the company details
                                company_details = company_driver.find_name(
                                    domain)
                                # write in data in the file
                                writer.writerow(
                                    {"Domain": domain, "Company Details": company_details})
                        except BaseException as BS:
                            # close connetion to the driver in case something goes wrong
                            domain_driver.close_connection()
                            company_driver.close_connection()
                            print(BS)
            else:
                # an existing file has been opened in append mode
                with open("output.csv", mode="a", newline="") as o_file:
                    # creating a writer object to write in the existing file
                    writer = csv.writer(o_file)
                    # iterate over the input file and write the rows
                    for i in reader:
                        try:
                            # random sleep
                            time.sleep(secrets.choice(times))
                            # first generate the domain name
                            domain = domain_driver.find_domain(i[0])
                            # furher operation only when valid domain found
                            if domain != "Domain not found":
                                # generate the company details
                                company_details = company_driver.find_name(
                                    domain)
                                # write data in file
                                writer.writerow([domain, company_details])
                        except BaseException as BS:
                            # close connetion to the driver in case something goes wrong
                            domain_driver.close_connection()
                            company_driver.close_connection()
                            print(BS)

    # if everything goes well close the driver connection
    domain_driver.close_connection()
    company_driver.close_connection()


if __name__ == '__main__':
    main()

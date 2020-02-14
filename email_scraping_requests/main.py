from requests_html import HTMLSession
from collections import defaultdict
import csv

"""This script will fetch the name of all partners and their email addresses from
from freshservice partner search portal (https://www.freshworks.com/company/partners/find-partners/).
"""

URL = "https://www.freshworks.com/company/partners/find-partners/"

# storing the email and name.
dataset = defaultdict(list)


def email_parser(email):
    """[Email parsing function]

    Arguments:
        email {[str]} -- [email or list of email addresses]
    """
    return [i.strip() for i in email.split(',')]


def get(elem):
    try:
        return elem.pop(0)
    except:
        return "None"


def main(url=URL):
    # creating a session
    session = HTMLSession()
    # making a get request with the URL
    resp = session.get(url)
    # caption all content elements and iterate over them
    for item in resp.html.xpath('//div[@class="partner-card mb-xl"]'):
        email = get(item.xpath('.//a[contains(@href, "@")]/text()'))
        name = get(item.xpath('.//div[@class="reseller-info"]/h6/text()'))
        # parsing email data
        p_emails = email_parser(email)
        if len(p_emails) > 1:
            for e in p_emails:
                dataset[e].append(name)
        else:
            dataset[p_emails[0]].append(name)
    return None


def write_to_csv(dataset):
    """[writing dataset in a csv file]

    Arguments:
        dataset {[defaultdict]} -- [key value pair of email and name]
    """
    with open("dataset.csv", mode='w', newline='', encoding="utf-8") as w_file:
        # definging the heading of the file
        heading = ['Name', 'Email']
        # creating a csv writer object
        writer = csv.DictWriter(w_file, fieldnames=heading)
        # writing the first row
        writer.writeheader()
        for key, value in dataset.items():
            writer.writerow({'Name': ', '.join(value), 'Email': key})

    return None


if __name__ == "__main__":
    main()
    write_to_csv(dataset)

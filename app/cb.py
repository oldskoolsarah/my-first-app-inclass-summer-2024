
import bs4 #contains beautifulsoup
import requests
from pandas import DataFrame

import os
from dotenv import load_dotenv

load_dotenv()

def load_beast_data():

    import requests
    from bs4 import BeautifulSoup
    
    # pull in data from CB wiki page
    request_url = "https://wiki.cassettebeasts.com/wiki/Species"

    response = requests.get(request_url)
    # response.status_code (should be 200 if successful)

    # use beautiful soup package to pull contents into a table
    soup = BeautifulSoup(response.text)

    # parse the web page data for the table and pull this into a variable for further ETL
    table = soup.find("table")

    # pull rows of the table into an index, tr = table rows
    rows = table.find_all("tr")

    # create header row index
    header_row = rows[0]

    # create header names, th = table header
    header_names = [th.text.strip() for th in header_row.find_all("th")]

    # rename the first one, which was ""
    header_names[0] = "Image URL" 

    # create new records table to hold monster data that was fetched above
    records = []

    # for loop that recreates the table
    for tr in rows[1:]:
        values = [td.text.strip() for td in tr.find_all("td")]
        # overwrite image value because it needs a diff strategy:
        try:
            img_path = tr.find("img").attrs["src"] 
            img_url = "https://wiki.cassettebeasts.com" + img_path
        except:
            img_url = None
        values[0] = img_url # first column is the image

        record = {}
        for k,v in zip(header_names, values):
            record[k] = v
        records.append(record)

    
    #print(records)
    return records
    #return records[0:5]

def print_beast_data():

    from pandas import DataFrame

    records = load_beast_data()

    df = DataFrame(records)
    df.index.name = "Id"
    df.head()
    #print(df)

    return df


def fetch_beast_data(records):

    # fake user input
    user_beast_name_input = "Springheel"
    user_beast_number_input = "001"
    search_successful = False

    for tr in records[tr]:
        if (records[tr] == user_beast_number_input):

            search_successful = True
            return records[tr]


    if (search_successful == False):
            print("Could not find entered beast. Please try again.")


load_beast_data()
#print_beast_data()

if __name__ == "__main__":

    
    # only if running from command line will this get reached

    # BEAST SELECTION

    #number = input("Please input a number (e.g. '001'): ")
    #print("NUMBER:", number)

    # REPORT

    #df = print_beast_data()

    #print(df.columns)
    #print(len(df))
    #df.head()

    print_beast_data()


'''
Question 4 -
Write a program to download the data from the link given below and then read the data and convert the into
the proper structure and return it as a CSV file.
Link - https://data.nasa.gov/resource/y77d-th95.json
Note - Write code comments wherever needed for code understanding.

Excepted Output Data Attributes
● Name of Earth Meteorite - string id - ID of Earth
● Meteorite - int nametype - string recclass - string
● mass - Mass of Earth Meteorite - float year - Year at which Earth
● Meteorite was hit - datetime format reclat - float recclong - float
● point coordinates - list of int
'''

import requests
import pandas as pd

URL = "https://data.nasa.gov/resource/y77d-th95.json"

try:
    #download the data using request.get from the url
    response = requests.get(URL)
except requests.ConnectionError as e:
    print("Connection error, please try after sometimes...")
except requests.Timeout as e:
    print("Connection timeout error, please try after sometimes...")
else:
    # Convert the response data into a pandas dataframe
    df = pd.json_normalize(response.json())
    print(df.head)

    # Saving the dataframe to an CSV file
    df.to_csv("nasa_ouput.csv")

    #read the data from the CSV to verify
    df_read = pd.read_csv("nasa_ouput.csv")
    print(df_read.head())
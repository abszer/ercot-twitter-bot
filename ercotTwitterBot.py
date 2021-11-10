import json
import requests
import twitter
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

#setup environemnt variable
load_dotenv()
consumer_key = os.environ.get("consumer_key")
consumer_secret = os.environ.get("consumer_secret")
access_token_key = os.environ.get("access_token_key")
access_token_secret = os.environ.get("access_token_secret")


#setup twitter api access
twitter_api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token_key, access_token_secret=access_token_secret)

#get data from ercot thru get request
r = requests.get("http://www.ercot.com/content/cdr/html/real_time_system_conditions.html")
soup = BeautifulSoup(r.text, 'html.parser')

table_data = []
for data in soup.find_all('td'):
     table_data.append(data.string)

#FREQUENCY
current_frequency = float(table_data[2])
instantaneous_time_error = float(table_data[4])
consec_BAAL_exceedances = float(table_data[6])
#REALTIME DATA
actual_system_demand = float(table_data[9])
total_system_capacity = float(table_data[11])
total_wind_output = float(table_data[13])
total_solar_output = float(table_data[15])
current_system_inertia = float(table_data[17])
#DC TIE FLOWS
dc_e = float(table_data[20])
dc_laredo = float(table_data[22])
dc_n = float(table_data[24])
dc_railroad = float(table_data[26])
dc_eaglepass = float(table_data[28])


print(current_frequency)

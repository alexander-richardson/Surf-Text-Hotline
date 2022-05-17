#Get weather information from Darksky

import os
from requests import get
from pathlib import Path
from dotenv import load_dotenv
import json

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

# mapping object that represents environmental variables. 
auth_token = os.environ['DARKSKY']

location = '45.761329389108795,-123.96687170533593'

#get information on location
resp = get('https://api.darksky.net/forecast/{}/{}?exclude=alerts,flags '.format(auth_token, location))

#turn response into a JSON object 
resp_json = json.loads(resp.text)

#Current Temperature
current_temp= int(resp_json['currently']['temperature'])

#Current weather summary
summary = resp_json['hourly']['summary'].lower()

weather_forcast = 'Out of the water its {}, expect {}'.format(current_temp, summary )


#print(current_temp)
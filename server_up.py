import requests
import time
import datetime
import re
from bs4 import BeautifulSoup

# Code checks if world in line 33 exists. Politeness = sleep for 2 seconds

world = "Famfrit"
isAvail = False

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

url = "https://na.finalfantasyxiv.com/lodestone/worldstatus/"

while isAvail == False: 
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    world_name_list = soup.find_all(class_="world-list__world_name")
    world_status_dict = soup.find_all(class_="world-list__create_character")

    for x in world_name_list:

        world_name = x.find('p').text
        
        if world_name == "Famfrit":
            
            index = world_name_list.index(x)

            world_status = world_status_dict[index]

            if "Unavailable" in str(world_status):
                print("World Unavailable")
            else:
                now = datetime.datetime.now()
                dt_string = now.strftime("%m-%d %H:%M")

                print("WORLD AVAILABLE... ", dt_string)
                
                isAvail = True
    time.sleep(2)





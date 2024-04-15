"""

Scrapes the GeoCache.com undocumented API and gets GeoCaches.

NOTE: This takes a long time.

REVERSE ENGINEERING NOTE:

I have no legal responsibility with what you do with this.

MORE NOTES:

After extensive reverse-engineering, here is what I found for authorization necessary:
- a User-Agent header
- a gpskauth key
- a jwt auth key

We may remove the gpskauth key for a while, as long as the jwt key is fresh and new.
After a while, it seems to expire, and only including gpskauth will help
"""
import json
import numpy as np
import requests
from requests.auth import HTTPBasicAuth
import auth_keys
import random
import time

step_size = 1

lats = np.arange(43.6568127,43.7442303,step_size)
longs = np.arange(-80.0581707,-79.7306951,step_size)


magic_word = "geocatchermagicword"

f = open("scrape.txt",'wb')

found = []

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def grab_geocaches(in_lat,in_long):
    url = f"https://www.geocaching.com/api/proxy/web/search/v2?skip=0&take=5000&asc=true&sort=distance&properties=callernote&origin={in_lat}%2C{in_long}&rad=1609300000.44"
    #print("Grab geocache API")
    #print(url)
    
    key_id = random.randint(0,len(auth_keys.auth_keys_jwt)-1)
    
    x = requests.get(url,headers=headers,cookies={"gspkauth":auth_keys.auth_keys_gspk[key_id],"jwt":auth_keys.auth_keys_jwt[key_id]})
    
    #x = requests.get(url,headers=headers,cookies=cookies) #For static testing

    #print(x.status_code)

    #print(x.encoding)

    if x.status_code != 200:
        print("Bad response code!",x.status_code)
        print("[DEBUG] Using auth index",key_id)
        time.sleep(10)

    if x.text != '{"results":[],"total":0}' and len(x.text) > 5:
        return x.text
    else:
        return 0

counter_premium = 0
counter_total = 0

counter_lats = 0

for lat in lats:
    counter_lats = counter_lats + 1
    for long in longs:
        print(lat,long)
        response = grab_geocaches(lat,long)
        #print(response)
        if response != 0:
            data = json.loads(response)
            try:
                for i in range(len(data["results"])):
                    #print("Found",data["results"][i]["name"])
                    
                    #found.append(data["results"][i]["name"])
                    #print(data["results"][i])
                    if data["results"][i]['premiumOnly'] == False:
                        try:
                            f.write(str(data["results"][i]["name"]+magic_word+data["results"][i]["code"]+magic_word+str(data["results"][i]["postedCoordinates"]["latitude"])+magic_word+str(data["results"][i]["postedCoordinates"]["longitude"])+"\n").encode(encoding='UTF-8'))
                            #print("Found OK geocache!")
                            counter_total = counter_total + 1
                        except Exception as e:
                            print(e)
                            print("Problematic string:")
                            print(data["results"][i])
                            #print("No coordinates or might have emojis :(")
                            pass
                    else:
                        #print("Found premium only")
                        #print(str(data["results"][i]))
                        #pass
                        counter_premium = counter_premium + 1
                        counter_total = counter_total + 1
            except:
                print("No data")
        print("Premium:",counter_premium)
        print("Total:",counter_total)
        print("Iterations:",str(counter_lats)+"/"+str(len(lats)))
f.close()

print("Premium:",counter_premium)
print("Total:",counter_total)
print("Done.")

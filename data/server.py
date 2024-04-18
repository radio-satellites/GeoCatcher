from flask import Flask
from flask_cors import CORS, cross_origin
import os
from flask import request
import geopy.distance
import difflib
from urllib.parse import unquote
import auth_keys
import random
import time
import requests
import json

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

f = open(os.path.dirname(os.path.realpath(__file__))+"/scrape_filtered.txt",'rb')

lines = f.read().decode(encoding="utf-8").split("\n")

magic_word = "geocatchermagicword"

names_list = []

for line in lines:
    fields = line.split(magic_word)
    names_list.append(fields[0])

#print(names_list[1])



"""Functions for live receiving"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def grab_geocaches(in_lat,in_long):
    url = f"https://www.geocaching.com/api/proxy/web/search/v2?skip=0&take=5000&asc=true&sort=distance&properties=callernote&origin={in_lat}%2C{in_long}&rad=16090.44"
    print("Grab geocache API")
    print(url)
    
    key_id = random.randint(0,len(auth_keys.auth_keys_jwt)-1)
    
    x = requests.get(url,headers=headers,cookies={"gspkauth":auth_keys.auth_keys_gspk[key_id],"jwt":auth_keys.auth_keys_jwt[key_id]})
    
    #x = requests.get(url,headers=headers,cookies=cookies) #For static testing

    #print(x.status_code)

    #print(x.encoding)

    if x.status_code != 200:
        print("Bad response code!",x.status_code)
        print("[DEBUG] Using auth index",key_id)

    if x.text != '{"results":[],"total":0}' and len(x.text) > 5:
        return x.text
    else:
        return 0

"""
#Disabled since V0.5.6
@app.route('/api/v1/getall')
@cross_origin()
def return_all():
    lines_all = ""
    for line in lines:
        lines_all = lines_all + line + "\n"
    return lines_all
"""
@app.route('/api/v1/ping')
@cross_origin()
def ping():
    return "OK"


@app.route('/api/v1/getmatches')
@cross_origin()
def getmatches():
    query_string = request.query_string
    query_string = query_string.split(b",")
    id = unquote(query_string[0].split(b"=")[1].decode())

    print("received id",id)

    match = difflib.get_close_matches(id, names_list)
    
    return str(match)


@app.route('/api/v1/getlive')
@cross_origin()
def getLive():
     #Get the coordinates and distance
    if len(request.query_string) > 3:
        query_string = request.query_string
        query_string = query_string.split(b",")
        lat = float(query_string[0].split(b"=")[1].decode())
        long = float(query_string[1].split(b"=")[1].decode())

        print("Debug: sending lat long",lat,long)

        response = grab_geocaches(lat,long)

        if response != 0:
            data = json.loads(response)

            #print(data)
            line = ""
            for i in range(len(data["results"])):
                    #print("Found",data["results"][i]["name"])
                    
                    #found.append(data["results"][i]["name"])
                    #print(data["results"][i])
                    if data["results"][i]['premiumOnly'] == False:
                        #print("Yay! Regular Geocache!")
                        try:
                            line += data["results"][i]["name"]+magic_word+data["results"][i]["code"]+magic_word+str(data["results"][i]["postedCoordinates"]["latitude"])+magic_word+str(data["results"][i]["postedCoordinates"]["longitude"])+"\n"

                        except:
                            print("Bad string.")
            return line

@app.route('/api/v1/getdistance')
@cross_origin()
def getClosest():
    """
    Returns the closest geocaches. 

    Note: I initially tried implementing a calculation algorithm (haversing and WGS-84) that checked the distance, 
    but that was too slow for so many geocaches. The algorithm now simply checks the latitude and longitude and sees
    whether or not the numbers are similar (within +-0.1)
    
    """
    #Get the coordinates and distance
    if len(request.query_string) > 3:
        query_string = request.query_string
        query_string = query_string.split(b",")
        lat = query_string[0].split(b"=")[1]
        long = query_string[1].split(b"=")[1]

        #Rather than building a distance table, return each geocache that is close(ish)

        print("Building distances table")
        geocaches = []

        for line in lines:
            try:
                fields = line.split(magic_word)
                #print(fields)
                coords_1 = (float(fields[2]),float(fields[3]))
                coords_2 = (float(lat),float(long))
                if abs(coords_1[0] - coords_2[0]) < 0.1 and abs(coords_1[1] - coords_2[1]) < 0.1:
                    geocaches.append(line)
            except Exception as e:
                print("GeoCache with invalid distance")
                print(line)
                print(e)
                pass
        
        lines_all = ""
        for line in geocaches:
            lines_all = lines_all + line + "\n"
        return lines_all

        
    else:
        return "Invalid API usage"



app.run()
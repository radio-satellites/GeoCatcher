from flask import Flask
from flask_cors import CORS, cross_origin
import os
from flask import request
import geopy.distance
app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

f = open(os.path.dirname(os.path.realpath(__file__))+"/scrape_filtered.txt",'rb')

lines = f.read().decode(encoding="utf-8").split("\n")

magic_word = "geocatchermagicword"

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
from math import radians, cos, sin, asin, sqrt

f = open("scrape.txt",'rb')


lines = f.read().decode(encoding="utf-8").split("\n")

filtered = list(set(lines))

closest = []

for line in filtered:
    

def dist(lat1, long1, lat2, long2):
    # convert decimal degrees to radians 
    lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])
    # haversine formula 
    dlon = long2 - long1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km

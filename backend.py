import http.client
import json
key = 'AmFLTg_M4bdEC_v6Clrb4ztBqB6tdf3aa2yDjvNV8Orf2uIYT0vt52PgUy_B1OPj'
conn = http.client.HTTPSConnection("dev.virtualearth.net")

def distance(lat1, long1, lat2, long2):
    payload = ''
    headers = {}
    link = "/REST/v1/Routes/DistanceMatrix?origins="
    dest = "&destinations="
    api = "&travelMode=driving&key=AmFLTg_M4bdEC_v6Clrb4ztBqB6tdf3aa2yDjvNV8Orf2uIYT0vt52PgUy_B1OPj"
    url2 = link + str(lat1) + "," + str(long1) + dest + str(lat2) + "," + str(long2) + api
    conn.request("GET", url2, payload, headers)

    res = conn.getresponse()
    data = res.read()
    data = json.loads(data.decode("utf-8"))
    return data["resourceSets"][0]["resources"][0]["results"][0]["travelDistance"]


blat=float(input("Enter origin Lat : "))
blong=float(input("Enter origin Long : "))
dlat=11.025343050133426                 #lat of fixed destination
dlong=77.01108569820228                 #long of fixed destination

alat=10.868216487642801                 #assumption of existing user's origin
along=76.88292254654007 

d1=distance(alat,along,dlat,dlong)
d2=distance(blat,blong,dlat,dlong)
d3=distance(alat,along,blat,blong)
if d1+d2<d2+d3 and d1+d2<d1+d3:
    print("Travel with your own vehicle for better environmental impact")
elif d2+d3<d1+d3:
    print("X will be able to pick you up")
else:
    print("You should pick X")
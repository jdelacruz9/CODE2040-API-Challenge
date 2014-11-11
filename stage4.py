#author:	Julio de la Cruz
#email: 	jjcnatera@gmail.com

import requests
import json
import datetime

#my identifying token
token = 'jcUHJ3Axst' 

#this is the JSON dictionary, with my token, that I will use to get the prefix and the array of strings
data = {
	'token': token
}

#r will have the requested array and the prefix
r = requests.post('http://challenge.code2040.org/api/time', json.dumps(data))

#the JSON dictionary received from the request
rJSON = r.json()['result']

#getting the datestamp from the dictionary
datestamp = rJSON['datestamp']
interval = rJSON['interval']

#printing the datestamp
print "The datestamp is %s" %(datestamp)

#printing the interval
print "The interval is %s" %(interval)

#since we know in which format datestamp is, ISO 8601, we can define its different parts
years = int(datestamp[:4])
months = int(datestamp[5:7])
days = int(datestamp[8:10])
hours = int(datestamp[11:13])
minutes = int(datestamp[14:16])
seconds = int(datestamp[17:19])
microseconds = int(datestamp[20:23])

#Now we have to make a datetime object
ObjDatestamp = datetime.datetime(years, months, days, hours, minutes, seconds, microseconds)

#We have a datetime object so we can use its methos to calculate the new datestamp
newDatestamp = ObjDatestamp + datetime.timedelta(seconds = interval)

#now we use the isoformat method on the new datestamp to get the new ISO 8601 datestamp string
finalDatestamp = newDatestamp.isoformat()

#printing the final datestamp
print "The new datestamp is %s" %(finalDatestamp) 
finalData = {
	'token': token,
	'datestamp': finalDatestamp
}

#response of the final request
response = requests.post('http://challenge.code2040.org/api/validatetime', json.dumps(finalData))

#lets see if I passed the stage 1
print response.json()
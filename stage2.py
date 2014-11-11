#author:	Julio de la Cruz
#email: 	jjcnatera@gmail.com

import requests
import json
from urllib2 import urlopen, Request

#my identifying token
token = 'jcUHJ3Axst' 

#this is the JSON dictionary, with my token, that I will use to get the string and the array
data = {
	'token': token
}

#r will have the requested array and the string
r = requests.post('http://challenge.code2040.org/api/haystack', json.dumps(data))

#the JSON dictionary received from the request
rJSON = r.json()['result']

#getting the haystack array and the needle string from the dictionary
haystack = rJSON['haystack']
needle = rJSON['needle']

print haystack
print needle

#Now we search the needle string in the haystack array using an array method to find its position.
pos = haystack.index(needle)
print pos
#Constructing the final JSON, to use in the final request
finalData = {
	'token': token,
	'needle': pos
}

#response of the final request
response = ('http://challenge.code2040.org/api/validateneedle', json.dumps(finalData))
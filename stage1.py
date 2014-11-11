#author:	Julio de la Cruz
#email: 	jjcnatera@gmail.com

import requests
import json

#my identifying token
token = 'jcUHJ3Axst' 

#this is the JSON dictionary, with my token, that I will use to get the string
data = {
	'token': token
}

#this is the response of the request that will contain the json with the string. I have
#post the request with the endpoint url and my dictionary. To use the dictionary in the 
#request I have to encode it, that's why I used json.dumps.  
r = requests.post('http://challenge.code2040.org/api/getstring', json.dumps(data))

#the string to be reversed, received in the request
string = r.json()['result']

#printing the string to be reversed
print "This is the string: %s" %(string)

#the reversed string
reversedString = string[::-1]

#printing the reversed string
print "This is the reversed string: %s" %(reversedString)

#final dictionary with my token and the reversed string to use in the final request 
finalData = {
	'token': token,
	'string': reversedString
}

#response of the final request
response = requests.post('http://challenge.code2040.org/api/validatestring', json.dumps(finalData))

#lets see if I passed the stage 1
print response.json()


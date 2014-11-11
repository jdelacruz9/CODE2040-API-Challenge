#author:	Julio de la Cruz
#email: 	jjcnatera@gmail.com

import requests
import json

#my identifying token
token = 'jcUHJ3Axst' 

#this is the JSON dictionary, with my token, that I will use to get the prefix and the array of strings
data = {
	'token': token
}

#r will have the requested array and the prefix
r = requests.post('http://challenge.code2040.org/api/prefix', json.dumps(data))

#the JSON dictionary received from the request
rJSON = r.json()['result']


#getting the array and the prefix from the dictionary
arrayOfStrings = rJSON['array']
prefix = rJSON['prefix']

#printing the array of strings
print "The array of strings is %s" %(arrayOfStrings)

#printing the prefix
print "The prefix is %s" %(prefix)

#the new array that will contain the strings that do not start with that prefix.
resArray = []

#searching for the strings that do not start with that prefix. If the prefix is not at the beginning of
#the string, the find method will return a value different from 0, which means that we can append the string 
#to our new array.
for string in arrayOfStrings:
	if(string.find(prefix)):
		resArray.append(string)

#printing the final array
print "The final array is %s" %(resArray)
#Constructing the final JSON, to use in the final request
finalData = {
	'token': token,
	'array': resArray
}

#response of the final request
response = requests.post('http://challenge.code2040.org/api/validateprefix', json.dumps(finalData))

#lets see if I passed the stage 1
print response.json()



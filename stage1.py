import requests
import json

token = 'jcUHJ3Axst'
url = 'http://challenge.code2040.org/api/getstring'
data = {
	'token': 'jcUHJ3Axst'
}
r = requests.post(url, json.dumps(data))
string = r.json()['result']
print string
reversedString = string[::-1]
print reversedString
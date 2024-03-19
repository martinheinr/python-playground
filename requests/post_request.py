import requests
import json

p = {"description": "white kitten", "name": "Snowball", "age_months": 6}

received_dictionary = {}

#So, if we need to send and receive data from a web service, we can turn our data into dictionaries and then pass that as the data attribute of a POST request.
#It's super common to send and receive data specifically in JSON format, so the 
#Requests module can do the conversion directly for us, using the json parameter.  
response = requests.post("https://example.com/path/to/api", json=p)

print(response.request.url)
print(response.request.body)
#received_dictionary = response.request.body.decode('utf-8')
received_dictionary = json.loads(response.request.body.decode('utf-8'))
print(received_dictionary["name"])
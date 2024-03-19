import requests

response = requests.get('https://example.com/path/to/api/cat_pictures?search=grey+kitten&max_results=15')
response_1 = requests.get('https://google.com')

response_code = response.status_code
#Raises http error only if response was not ok
some_text = response.raise_for_status()

#print(response_code)
#print(response.text[:100])
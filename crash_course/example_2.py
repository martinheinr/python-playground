# Check if a key exists in the dictionary and perform different actions based on the result
myDictionary={"banana":0}

key = 'banana'
if key in myDictionary:
	print(f"The value of {key} is {myDictionary[key]}")
else:
	print(f"{key} is not found in the dictionary")
	
key = 'banana'
if key in myDictionary:
	print("The value of {} is {}".format(key, myDictionary[key]))
else:
	print(f"{key} is not found in the dictionary")
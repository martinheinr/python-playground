#Define dictionary
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)

#If a key doesn't exist in the dictionary, element (key and value) will be added to the dictionary
file_counts["cfg"] = 8
print(file_counts)

#If a key exists in the dictionary, value will be replaced
file_counts["cfg"] = 1700
print(file_counts)

#Print elements value that is a pair of a key
print(file_counts["txt"])

#Remove element with del by providing a key
del file_counts["cfg"]
print(file_counts, "\n")

#Initiate enw dictionary
farm = {"cows":10, "chickens":14, "sheeps":2, "dogs":23}

#Iterate through a dictionary and print the keys in this case animals
for animals in farm:
  print(animals)

#Iterate through a dictionary and print the key and value for every item
#items() returns tuples
for animals, amount in farm.items():
  print("There are {} {} on the farm.".format(amount, animals))

farm_keys=farm.keys()
farm_values=farm.values()
print(farm_keys)
print(farm_values)

#Iterate through a dictionary and print the values for each element
for value in file_counts.values():
    print(value)

def count_letters(text):
    result = {}
    #Iterrate throug text, which is a string
    for letter in text:
        #For each lettter check if it is in the result
        if letter not in result:
            #If not in the result set the value to 0
            result[letter] = 0
        #Increase the value +1
        result[letter] += 1
    return result
print(count_letters("aaaaa"))
print(count_letters("tenant"))
print(count_letters("a long string with a lot of letters"))

my_dictionary = {"keyA":["value1", "value2"], "keyB":["value3", "value4"]}
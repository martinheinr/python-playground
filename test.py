def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while start >= stop:  # Complete the while loop
            return_string = return_string + str(start) # Add the numbers to the "return_string"
            if start > stop:
                return_string += ","
            start = start -1 # Increment the appropriate variable
    else:
        return_string = "Counting up: "
        while start <= stop: # Complete the while loop
            return_string = return_string + str(start)# Add the numbers to the "return_string"
            if start < stop:
                return_string += ","
            start= start +1 # Increment the appropriate variable
    return return_string


#print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
#print(counter(2, 1)) # Should be "Counting down: 2,1"
#print(counter(5, 5)) # Should be "Counting up: 5"

def count_numbers(first, last):
  # Loop through the numbers from first to last 
  x = first
  while x <= last:
    print(x)
    x = x +1

#count_numbers(2, 6) 


filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.

new_filenames = []
new_string=""
for filename in filenames:
    if filename.endswith("hpp"):
        new_string=filename.replace(".hpp",".h")
        new_filenames.append(new_string)
    else:
        new_filenames.append(filename)


def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  print (words)
  for word in words:
    # Create the pig latin word and add it to the list
    word = word[1:] + word[0] + "ay "
    # Turn the list back into a phrase
    say = say + word
  return say
    
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
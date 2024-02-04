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



count_numbers(2, 6) 
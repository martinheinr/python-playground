def skip_elements(elements):
    #Intialize empty list
    result = []
    #Iterate with loop through elements with enumeration function
    #Enumerate function first returns index of an element in a sequence and then the element in the sequence
    for index, element in enumerate(elements):
        #Modulo condition filters to output every second index
        if index % 2 == 0:
            #If true, appent to the list
            result.append(element)
    return result
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
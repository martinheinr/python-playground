def skip_elements(elements):
    #Intialize empty list
    result = []
    #iterate with loop through elements with enumeration function
    #enumerate function first returns index of an element in a sequence and then the element in the sequence
    for index, element in enumerate(elements):
        #modulo condition filters to output every second index
        if index % 2 == 0:
            result.append(element)
    return result
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
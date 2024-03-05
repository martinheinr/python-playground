import sys

def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1


def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise.

    List must be sorted.
    """
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2
        
        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1
   


# Original list
list_for_test = ["aa", "ab", "ac", "ad", "bb", "ba", "bc", "dd", "da", "de", "dq", "ee"]

# Sort the original list
list_for_test.sort()

# Make a copy of the sorted list
sorted_list = list_for_test.copy()

# Print sorted list 
#print(sorted_list)


index = (binary_search(sorted_list, "da"))

print(sorted_list)
print("index:", index, list_for_test[index])
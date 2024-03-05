def find_item(list, item):
    # Returns True if the item is in the list, False if not.
    if len(list) == 0:
        return False

    # Is the item in the center of the list?
    middle = len(list) // 2

    if list[middle] == item:
        return True
    elif item < list[middle]:
        # Call the function with the first half of the list
        return find_item(list[:middle], item)
    else:
        # Call the function with the second half of the list
        return find_item(list[middle + 1:], item)

# Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan", "BB", "Chris", "Terry", "Jamie", "Jordan", "Alex"]

print(find_item(list_of_names, "Alex"))   # True
print(find_item(list_of_names, "Andrew")) # False
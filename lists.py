x = ["Now", "we", "are", "cooking!"]
print(type(x))
print(len(x))
print(x[0])

#Append to a list
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)

#Insert to a list
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
print(fruits)

#Remove from a list
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.remove("Apple")
print(fruits)

#Pop from a list - pop method has to receive index
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.pop(1)
print(fruits)

#Sorting lists
def sort_distance(distances):
    distances.sort() # Sort the list
    distances.reverse() # Reverse the order of the list
    return distances


print(sort_distance([2,4,0,15,8,9]))
# Should print [15, 9, 8, 4, 2, 0]
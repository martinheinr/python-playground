import operator

fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
a=sorted(fruit.items(), key=operator.itemgetter(1))

b=sorted(fruit.items(), key=lambda x: x[1], reverse=True)
print(b)
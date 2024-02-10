filepath = "C:\\test_files\\spider.txt"
file = open(filepath)
#print(file.readline())
#print(file.read())
file.close()

#Iterrate through file
with open(filepath) as file:
    for line in file:
        print(line.upper())

with open(filepath) as file:
    for line in file:
        print(line.strip().upper())

file = open(filepath)
lines = file.readlines()
lines.sort()
print(lines)

with open(filepath, "w") as file:
    file.write("It was a dark and stormy night")

with open (filepath) as file:
    print(file.readline())
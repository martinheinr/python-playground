original_string = "Hello, world!"
new_string = original_string.replace("world", "Python")

print(new_string)


animals = "lions, tigers and bears"
index = animals.index("bears")
new_animal = "bird"
animals = animals[:index] + new_animal

print(animals)
print("tigers" in animals)
print("snakes" in animals)

answer = "NO"
if answer == "yes":
  print("User said yes")
elif answer.lower() == "yes":
  print("User said yes")
else:
  print("User said " + answer)

test_string = ""
test_string = "...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"])
print(test_string)

crazy = int("12345") + int("54321")
print(crazy)

if "My be rest".endswith("rest"):
    print(True)
else:
    print(False)

test_x = "This is another example".split()
print(test_x)
print(test_x[1])

name = "Manny"
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))

#Formatting string with rounding
price = 7.5
with_tax = price * 1.09
print(price, with_tax)
#Formatting expression ${:.2f} starts with : following with .2f which means we are formatting float number and there should be 2 digits
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  #{:>3} formatting expression that aligns the expressions output 3 spaces to the right
  #In Python, the colon (:) is used in the context of string formatting to indicate the beginning of the format specification. 
  print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))


  def nametag(first_name, last_name):
    return("{} {}.".format(first_name, last_name[0]))


print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 

sentence = "My be rest"
if sentence.endswith("rest"):
    index=sentence.endswith("rest")
    print(True)
    print(int)
else:
    print(False)
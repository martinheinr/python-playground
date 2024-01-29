def test():
    friends = ['Jim', 'Bob', 'Tim']
    for n in friends:
        print("Hi " + n)

test()

name:str="test"
print(name)

download_size_kb = 200*1024
total_computers = 200
total_kbs = download_size_kb*total_computers

print(total_kbs) # Should print 40960000.0

bill = 47.28 # Assign "bill" variable with bill amount
tip = bill * 0.15 # Multiply by stated tip rate 
total = bill + tip # Sum the "total" of the "bill" and "tip"
share = total / 2 # Divide "total" by number of friends dining
print("Each person needs to pay: ", share) # Enter the required string and "share" 
# Hint: Remember to convert incompatible data types

print("blpha">"zeta")
def numbers(number):
    if number > 11: 
        print(0)
    elif number != 10:
        print(1)
    elif number >= 20 or number < 12:
        print(2)
    else:
        print(3)

numbers(10)

print("A dog" < "A mouse")
print(9999+8888 > 100*100)
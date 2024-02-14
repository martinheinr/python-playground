import re
result = re.search(r"aza", "plaza")
print(result)

result_2 = re.search(r"aza", "maze")
print(result_2)

print(re.search(r"^x", "xenon"))

print(re.search(r"p.ng", "clapping"))
print(re.search(r"^c..pp", "clapping"))
print(re.search(r"p.ng", "Ponge", re.IGNORECASE))

print("Testing character classes: ", re.search(r"[Pp]ython", "This is a pure sentence with Python."))


print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))
print(re.findall(r"cat|dog", "I like both dogs and cats."))

def check_punctuation (text):
  result = re.search(r"[^a-zA-Z-0-9 ]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False

#match Py followed by any number (as many as possible) of any characters ending with n
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))

#checks if the text passed includes the letter "a" 
print(re.search(r"[Aa].*[Aa]", "banana"))

#match Py followed by any number (as many as possible) of any characters ending with n, excluding spaces and other
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))

#matches as many characters but only if they appear one after another
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))

#? makes p optional in the following expressions
print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))
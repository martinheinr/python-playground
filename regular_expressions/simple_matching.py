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

#checks if the text passed includes the letter "a" twice
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

print("\n" + "\t" + "Following examples for escaping characters")

#backslash is used to escape special characters however keep in mind \n is new line while \t is tab
print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))

#\w matches numbers letters and underscores
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))

#match at least 2 groups of alphanumeric characters separated by one or more whitespace characters
print(re.search(r"\w\s", "123  Ready Set GO"))

print("\n")
#match countries that start with a and end with a
print(re.search(r"A.*a", "Argentina"))
#since there is a second last letter it is mathced, we need to make it stricter
print(re.search(r"A.*a", "Azerbaijan"))

#Adding beggining of the line and ending of the line then it should work
print(re.search(r"^A.*a$", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia"))

print("\n")
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
#spaces don't match with the pattern
print(re.search(pattern, "this isn't a valid variable"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1"))

#check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter
#followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point. 
print(re.search(r"^[A-Z][a-z\s]*[\?.!]$", "Is this is a sentence?")) # True
def divide(a, b):
	assert b != 0, "Cannot divide by zero"
	return a / b
print(divide(0, 4))

import re
def rearrange_name(name):
 result = re.search(r"^([\w .]*), ([\w .]*)$", name)
 return "{} {}".format(result[2], result[1])


rearranged_name = rearrange_name("Lovelace, Ada")
print(rearranged_name)
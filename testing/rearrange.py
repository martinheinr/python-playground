import re

def rearrange_name(name):
  if type(name)==int:
    return "Numbers are not supported"
  
  result = re.search(r"^([\w .]*), ([\w .]*)$", name)
  
  if result is None:
    return name
  return "{} {}".format(result[2], result[1])

print(rearrange_name(1))
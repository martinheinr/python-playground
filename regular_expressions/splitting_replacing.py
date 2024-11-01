import re
re.split(r"[.?!]", "One sentence. Another one? And the last one!")

re.split(r"([.?!])", "One sentence. Another one? And the last one!")

re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com")

test = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
print(test)


import re
def transform_record(record):
  #regex=r"(\d{3})-(\d{3,})-(\d{,7})"
  regex=r"(\d{3})-(\d)"
  new_record = re.sub(regex, r"+1-\1-\2", record)
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer
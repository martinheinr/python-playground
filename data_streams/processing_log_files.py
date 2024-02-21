import re
import sys

""" pattern = r"USER \((\w+)\)$"
line = "Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)"
result = re.search(pattern, line)
print(result[1])
 """
logfile = sys.argv[1]
usernames = {}
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    pattern = r"USER \((\w+)\)"
    result = re.search(pattern, line)

    if result is None:
      continue
    #print(result[1])
    name = result[1]
    
    """
    usernames.get(name, 0): The .get() method of dictionaries in Python is used to retrieve the value associated 
    with a given key. If the key (name in this case) exists in the dictionary (usernames), it returns the corresponding value. 
    If the key does not exist, it returns the default value specified as the second argument (in this case, 0). 
    usernames.get(name, 0) + 1: This expression retrieves the count associated with the username name in the 
    usernames dictionary (or 0 if the username doesn't exist yet) and then increments it by 1.
    """    
    usernames[name] = usernames.get(name, 0) + 1
    
    print(usernames)
import re
print(re.search(r"([0-9]\:[0-5][0-9])", "9:51"))
print(re.search(r"([1-2][0-9]\:[0-5][0-9])", "12:51"))
print(re.search(r"([1-2]?[0-9]\:[0-5][0-9])", "9:51"))


def check_time(text):
  pattern = r"[1-2]?[0-9]\:[0-5][0-9]\s?[AMPMampm]"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False

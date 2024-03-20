#Simple try -> except
try:
  print(x)
except NameError:
  print("Variable x is not defined")

#If the file is not found, it prints a message. If there is any other error (such as “permission denied”), 
#it prints the actual error. Finally, if there is no exception, it closes the file.
try:
  f = open("/etc/hosts", "w+")
  f.write("Success!")
except FileNotFoundError:
  print("Data file not found")
except Exception as ex:
  print("Error appending to file: " + str(ex))
else:
  f.close()
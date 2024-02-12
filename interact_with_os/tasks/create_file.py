import os

def new_directory(directory, filename):
  #Define path to the destination directory
  dest_dir = os.path.join(os.getcwd(), directory)
  
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(dest_dir) == False:
    os.mkdir(dest_dir)

  # Create the new file inside of the new directory
  os.chdir(dest_dir)
  with open (filename, "w") as file:
    pass

  # Return the list of files in the new directory
  return os.listdir(dest_dir)

print(new_directory("PythonPrograms", "script.py"))


import datetime

def file_date(filename):
  # Create the file in the current directory
  with open (filename, "w") as file:
    pass

  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  file_date_time = datetime.datetime.fromtimestamp(timestamp)

  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(str(file_date_time)[0:10]))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd
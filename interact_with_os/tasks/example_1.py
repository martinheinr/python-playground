import os

def create_python_script(filename):
  filepath = os.path.join(os.getcwd(), filename)
  comments = "# Start of a new Python program"
  with open (filepath, "w") as file:
    file.write(comments)

  filesize = os.path.getsize(filepath)
  return(filesize)   

print(create_python_script("program.py"))
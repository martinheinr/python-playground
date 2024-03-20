import logging

# Set the minimum logging level to INFO,
logging.basicConfig(level=logging.INFO)

# Get a logger object
#The __name__ parameter adds your Python module name to the logger’s output, 
#so if your module is called stuff.py, your log would include “[stuff]” in its output. 
log = logging.getLogger(__name__)

# Start the log file
log.info("Hello world")

try:
  # Try to append to a file that is normally not writable
  # for anyone other than root 
  f = open("/etc/hosts", "w+")
except IOError as ex:
  # The variable "ex" will hold details about the error
  # that occurred
  print("Error appending to file: " + str(ex))
else:
  # If there was no exception, close the file.
  f.close()

user = {"last_name": "Bana"}
try:
  first_name = user["first_name"]
except KeyError:
  print("User does not have a first_name field")
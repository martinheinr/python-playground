x = "hello"

""" if not isinstance(x, int):
  raise TypeError("Only integers are allowed") """


#If it is not an integer, the function raises a TypeError exception. 
#The function then checks to make sure that the port number is between 1024 and 65535. 
#This is because port numbers below 1024 are typically reserved for system services. 
#If the port number is outside of this range, the function raises a ValueError exception.

def start_server(port):
  if not isinstance(port, int):
    raise TypeError("Port number must be an integer")
  elif port < 1024 or port > 65535:
    raise ValueError("Port number is invalid")
start_server("asd")
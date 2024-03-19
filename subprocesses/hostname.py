import subprocess
import socket

def getMyIP(hostname):
    return socket.gethostbyname(hostname)

result = subprocess.run(['hostname'], stdout=subprocess.PIPE)
string = result.stdout.decode().strip()
#print(result.stdout.decode())
print(string)

myIp = getMyIP(string)
print(myIp)
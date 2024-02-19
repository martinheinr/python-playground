#All the commands like date, ls and host are Linux commands so the example runs in WSL

import subprocess
""" subprocess.run(["date"])
subprocess.run(["sleep", "2"])
result = subprocess.run(["ls", "this_file_does_not_exist"])
print(result.returncode) """

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout)

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout.decode().split())


result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stderr)
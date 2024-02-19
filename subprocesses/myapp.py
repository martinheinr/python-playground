#All commands like PATH is Linux command so the example runs in WSL


import os
import subprocess

""" my_env = os.environ.copy()
print(my_env)
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env) """

process_popen = subprocess.Popen(['echo', 'Hello from popen!'], stdout=subprocess.PIPE, text=True)

output_popen, _ = process_popen.communicate()

output_popen.strip()  # Extracting the stdout and stripping any extra whitespace

print(output_popen)
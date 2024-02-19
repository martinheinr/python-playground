import subprocess
import time

process = subprocess.Popen(['sleep', '5'])

message_1 = "The process is running in the background..."

print(message_1)

# Give it a couple of seconds to demonstrate the asynchronous behavior

time.sleep(6)

# Check if the process has finished

print("Checking if the process is still running...")

if process.poll() is None:

	message_2 = "The process is still running."

else:

	message_2 = "The process has finished."

print(message_2)
import os

filepath = "C:\\test_files\\spider.txt"


def check_path(file_path):
    if os.path.exists("ww"):
        print("File exists")
    else:
        print("File doesn't exist")

check_path(filepath)

file_size = os.path.getsize(filepath)
print(file_size)
#This code will provide the file size
file_timestamp = os.path.getmtime(filepath)
#This code will provide a timestamp for the file
print(file_timestamp)

import datetime
timestamp = os.path.getmtime(filepath)
file_date_time = datetime.datetime.fromtimestamp(timestamp)
#This code will provide the date and time for the file in an easy too understand format
print(file_date_time)

absolute_path = os.path.abspath(filepath)
#This code takes the file name and turns it into an absolute path
print(absolute_path)
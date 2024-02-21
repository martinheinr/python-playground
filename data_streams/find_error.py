#!/usr/bin/env python3
import sys
import os
import re


def error_search(log_file):
    error = input("What is the error? ")
    returned_errors = []
    error_patterns = [] + [error_word.lower() for error_word in error.split()]

    print("Your error pattern is: ", error_patterns)
    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            if any(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
    return returned_errors


  
def file_output(returned_errors):
  with open(os.path.expanduser('C:/test_files') + '/errors_found.log', 'w') as file:
    for error in returned_errors:
      file.write(error)
    file.close()
if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)

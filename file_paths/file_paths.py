import os
#Two ways to define absolute path on Windows
path_1 = "C:\\test_files\\files_x.txt"
path_2 = "C:/test_files/files_x.txt"

print(os.path.isfile(path_1))
print(os.path.isfile(path_2))

#init dictionary
outputs={}

#store current working directory in the dictionary under the key 'current_directory_before'
outputs['current_directory_before'] = os.getcwd()
print(outputs['current_directory_before'])

#store the list of files and directories in the current working directory in the dictionary under the key 'files_and_directories'
outputs['files_and_directories'] = os.listdir()
print(outputs['files_and_directories'])

outputs['path_value'] = os.environ.get('PATH')
print(outputs['path_value'])

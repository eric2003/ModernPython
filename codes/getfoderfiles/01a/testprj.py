import os

directory = 'vtkfiles'

file_names = os.listdir(directory)

for file_name in file_names:
    print(file_name)
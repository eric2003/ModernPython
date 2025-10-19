import subprocess
import os

exe_path = "ReadAllUnstructuredGridTypes.exe"

directory = 'vtkfiles'

file_names = os.listdir(directory)

for file_name in file_names:
    print(file_name)
    fullname = directory + "/" + file_name
    print("fullname=",fullname)
    parameters = [fullname]
    subprocess.run([exe_path] + parameters)



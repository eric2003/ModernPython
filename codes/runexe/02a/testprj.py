import subprocess
import os

exe_path = r"d:\work\vtk_2024_work\ModernVTK\codes\examples\IO\ReadAllUnstructuredGridTypes\01\build\Release\ReadAllUnstructuredGridTypes.exe"
directory = r"d:\work\vtk_2024_work\vtk-eample-data\vtkfiles"

file_names = os.listdir(directory)

for file_name in file_names:
    print(file_name)
    fullname = directory + "/" + file_name
    print("fullname=",fullname)
    parameters = [fullname]
    subprocess.run([exe_path] + parameters)



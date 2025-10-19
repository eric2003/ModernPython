import subprocess

exe_path = "ReadAllUnstructuredGridTypes.exe"

dir1 = "vtkfiles"

filename = "VTKCellTypes.vtk"
fullname = dir1 + "/" + filename
print("fullname=",fullname)

parameters = [fullname]

subprocess.run([exe_path] + parameters)


filename = "v.vtk"
fullname = dir1 + "/" + filename
print("fullname=",fullname)

parameters = [fullname]

subprocess.run([exe_path] + parameters)

filename = "uGridEx.vtk"
fullname = dir1 + "/" + filename
print("fullname=",fullname)

parameters = [fullname]

subprocess.run([exe_path] + parameters)



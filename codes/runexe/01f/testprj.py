import subprocess

exe_path = "ReadAllUnstructuredGridTypes.exe"

dir1 = "vtkfiles"

filenames = []
filenames.append("VTKCellTypes.vtk")
filenames.append("v.vtk")
filenames.append("uGridEx.vtk")

for filename in filenames:
    print(filename)
    fullname = dir1 + "/" + filename
    print("fullname=",fullname)
    parameters = [fullname]
    subprocess.run([exe_path] + parameters)



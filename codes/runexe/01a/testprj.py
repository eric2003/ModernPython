import subprocess

exe_path = "ReadAllUnstructuredGridTypes.exe"

parameters1 = ["VTKCellTypes.vtk"]
parameters2 = ["v.vtk"]
parameters3 = ["uGridEx.vtk"]

subprocess.run([exe_path] + parameters1)
subprocess.run([exe_path] + parameters2)
subprocess.run([exe_path] + parameters3)
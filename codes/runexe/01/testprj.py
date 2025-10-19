import subprocess

exe_path = "ReadAllUnstructuredGridTypes.exe"

#parameters = ["VTKCellTypes.vtk", "v.vtk", "uGridEx.vtk"]
parameters = ["VTKCellTypes.vtk"]

subprocess.run([exe_path] + parameters)
vtkString = "VTK:xyDICOM"

vtkString_split1 = vtkString.split(":")
vtkString_split2 = vtkString.split(":x")
vtkString_split3 = vtkString.split(":xy")

print(vtkString)
print(vtkString_split1)
print(vtkString_split2)
print(vtkString_split3)

print(type(vtkString_split1))
print(type(vtkString_split2))
print(type(vtkString_split3))


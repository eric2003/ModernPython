import re

text = "VTK::DICOM;VTK::zlib"
words = re.split(';|,| |VTK::', text)
new_list = [item for item in words if item]
print(words)
print(new_list)
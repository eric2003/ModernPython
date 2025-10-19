import re

text = "VTK::DICOM;VTK::zlib;VTK::MomentInvariants;VTK::eigen;VTK::kissfft;"
words = re.split(';|,| |VTK::', text)
new_list = [item for item in words if item]
print(words)
print(new_list)
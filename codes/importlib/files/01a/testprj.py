from importlib.metadata import files 
fs=files('wheel')
for myfile in fs:
   print ('current file: %s'% myfile)

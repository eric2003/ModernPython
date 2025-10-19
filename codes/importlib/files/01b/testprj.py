from importlib.metadata import files 
fs=files('wheel')
for p in fs:
   if 'utils.py' in str(p):
       print ('current file: %s'% p)


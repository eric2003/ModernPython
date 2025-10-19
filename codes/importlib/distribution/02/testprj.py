from importlib.metadata import distribution 
dist = distribution('wheel')
dm = dist.metadata['Requires-Python']
print("dm=",dm)
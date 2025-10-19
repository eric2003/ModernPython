from importlib.metadata import distribution 
dist = distribution('wheel')
print("dist.version=",dist.version)
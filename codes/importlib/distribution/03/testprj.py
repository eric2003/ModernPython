from importlib.metadata import distribution 
dist = distribution('wheel')
print("dist.metadata=",dist.metadata)
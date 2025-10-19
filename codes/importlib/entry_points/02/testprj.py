from importlib.metadata import entry_points 
eps = entry_points()
gp = sorted(eps.groups)
print("gp=",gp)
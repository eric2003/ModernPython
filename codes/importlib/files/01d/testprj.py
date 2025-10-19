from importlib.metadata import files 
fs=files('wheel')
util = [p for p in files('wheel') if 'utils.py' in str(p)][0]  
print("util=",util)
print("type(util)=",type(util))
print("util.size=",util.size)
print("util.dist=",util.dist)
print("util.dist=",util.hash)
#print(util.read_text())
print("util.locate()=",util.locate())

import matplotlib.pyplot as plt

x=[]
r=[]
u=[]
m=[]
p=[]
with open('sod_theory.plt', 'r') as f:
    for index, line in enumerate(f):
        words = line.strip().split()
        x.append( float(words[0]) )
        r.append( float(words[1]) )
        u.append( float(words[2]) )
        m.append( float(words[3]) )
        p.append( float(words[4]) )
        
print(x)
print(len(x))

plt.plot(x, r, linewidth=1.0, label="theory")
plt.xlabel("$x$")
plt.ylabel(r"$\rho$")
plt.legend()
plt.show()
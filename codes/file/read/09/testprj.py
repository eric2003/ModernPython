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
        
plt.figure("Exact solution for the Sod's shock-tube problem", figsize=(10, 8), dpi=100)
plt.subplot(2, 2, 1)
plt.plot(x, r, linewidth=1.0, label="density")
plt.xlabel("$x$")
plt.ylabel(r"$\rho$")
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(x, u, linewidth=1.0, label="velocity")
plt.xlabel("$x$")
plt.ylabel(r"$u$")
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(x, m, linewidth=1.0, label="mach number")
plt.xlabel("$x$")
plt.ylabel(r"$m$")
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(x, p, linewidth=1.0, label="pressure")
plt.xlabel("$x$")
plt.ylabel(r"$p$")
plt.legend()

plt.tight_layout()

plt.show()
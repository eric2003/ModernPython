import arithmetic.addfile
import arithmetic.subfile
import arithmetic.addfile as add
import arithmetic.subfile as sub
x = 2
y = 1
z1 = arithmetic.addfile.add(x, y)
z2 = arithmetic.subfile.sub(x, y)
z3 = add.add(x, y)
z4 = sub.sub(x, y)

print("z1 =", z1)
print("z2 =", z2)
print("z3 =", z3)
print("z4 =", z4)
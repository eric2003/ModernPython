import sys
import os
#sys.path.append("..")
sys.path.append("../..")
path1 = os.path.abspath('.')
path2 = os.path.abspath('..')
path3 = os.path.abspath('../..')
print('path1=',path1)
print('path2=',path2)
print('path3=',path3)

import arithmetic.addfile as add
import arithmetic.subfile as sub

add = add.add
sub = sub.sub

x = 2
y = 1
z1 = add(x, y)
z2 = sub(x, y)

print("z1 =", z1)
print("z2 =", z2)

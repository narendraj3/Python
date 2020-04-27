from array import *

jn = array("i",[5,4,3,2,1])

del jn[2]
print(jn)
jnn = array("i",[])
a = 2
for i in range(len(jn)):
    if i!=a:
        jnn.append(i)
print(jnn)
        


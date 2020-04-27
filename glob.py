
j = 3
m = 12
t = 55

def hi():
    global j
    j = 10
    m = 24
    t = 88
    x = globals() ['j']
    #'m','t']
    print(x)
    print(id(x))
    globals()['j']=99
   # globals()['m']=77
    #globals()['t']=66
    print("in",j)
    print(id(j))


hi()

print("out",j)
print(id(j))


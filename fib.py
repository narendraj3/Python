from fact import *
def fib(x):
    j = 0
    n = 1
    print(j)
    print(n)
    for i in range(2,x):
        r = j+n
        j = n
        n = r
        print(r)

fact(10)


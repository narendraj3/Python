from functools import reduce
n= int(input("enter factorial number:"))
lis = range(1,n+1)
#res = list(lis)
#print(res)
#result=list(filter(lambda x:x%2==0,lis))
#y = map(lambda x:x*3,lis)

fact=reduce(lambda a,b:a*b,lis)
print("factorial of {} is: ".format(n),fact)
#print(result)
#print(y)


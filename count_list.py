def count(*lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

x,y = count(1,5,66,25,45,88)
print(x,y)


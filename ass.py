def names(lst):
    above=0
    below=0
    for i in lst:
        if len(i)>5:
            above+=1
            print(i)

        else:
            below+=1
            print("name below 5:",i)

    return above,below

profile = ['vikas','jaan','sachin','rohit','paaji','hitman','sehwag']

x,y =names(profile)
print("above={} and below={}".format(x,y))

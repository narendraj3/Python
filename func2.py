def person(name,**bio):
    print(name)
    for i,j in bio.items():
        print(i,j)


person('narendra',age=22,place='Kadapa',mobile=8465816153)

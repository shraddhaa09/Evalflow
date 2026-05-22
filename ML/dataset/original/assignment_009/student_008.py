name=input()
i=-1
rev=""
while abs(i)<=len(name):
    rev=rev+name[i]
    i=i-1
print(rev)
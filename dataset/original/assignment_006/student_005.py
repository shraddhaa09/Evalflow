x=int(input())
p=1

if x==0:
    print(1)
else:
    for i in range(1,x+1):
        p*=i
    print(p)
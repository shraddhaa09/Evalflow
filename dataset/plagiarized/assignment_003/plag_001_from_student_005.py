a = [10,20,30,40,50]

x = 30

s = 0
e = len(a)-1

while(s<=e):

    m = int((s+e)/2)

    if(a[m]==x):
        print("found")
        break

    elif(a[m]<x):
        s = m+1

    else:
        e = m-1
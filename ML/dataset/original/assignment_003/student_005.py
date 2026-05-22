a = [11,22,33,44,55,66]

s = 0
e = len(a)-1

x = 44

while(s<=e):

    mid = int((s+e)/2)

    if(a[mid]==x):
        print("found")
        break

    elif(a[mid]>x):
        e = mid-1

    else:
        s = mid+1
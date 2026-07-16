arr=[1,2,3,4,5,6,7]

x=5

l=0
h=len(arr)-1

while l<=h:

    m=(l+h)//2

    if arr[m]==x:
        print("Found")
        break

    elif arr[m]<x:
        l=m+1

    else:
        h=m-1
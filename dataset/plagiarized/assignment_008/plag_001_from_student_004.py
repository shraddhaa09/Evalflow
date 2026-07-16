arr=[]

for i in range(5):
    x=int(input())
    arr.append(x)

big=arr[0]

for i in arr:
    if i>big:
        big=i

print(big)
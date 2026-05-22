arr=[]

for i in range(5):
    num=int(input())
    arr.append(num)

largest=arr[0]

for i in range(len(arr)):
    if arr[i]>largest:
        largest=arr[i]

print(largest)
arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input())
    arr.append(num)

for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

print(arr)
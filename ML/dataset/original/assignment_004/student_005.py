arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input())
    arr.append(value)

for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)
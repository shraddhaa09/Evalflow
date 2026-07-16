n = int(input("How many numbers: "))

arr = []

for i in range(n):
    arr.append(int(input()))

target = int(input("Enter search element: "))

low = 0
high = n - 1

while low <= high:

    mid = (low + high) // 2

    if arr[mid] == target:
        print("Element Found")
        break

    elif arr[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

if low > high:
    print("Not Found")
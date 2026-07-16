arr = [3, 5, 1, 9, 2]

for i in range(len(arr)):
    min1 = arr[i]

    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr)
def binary(arr, x):

    start = 0
    end = len(arr)-1

    while start <= end:

        middle = (start + end)//2

        if arr[middle] == x:
            return middle

        if x < arr[middle]:
            end = middle - 1

        else:
            start = middle + 1

    return -1


nums = [5, 15, 25, 35, 45]

result = binary(nums, 35)

if result == -1:
    print("Not found")
else:
    print("Found at", result)
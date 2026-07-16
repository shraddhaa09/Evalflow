def bsearch(arr, low, high, x):

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == x:
        return mid

    elif x < arr[mid]:
        return bsearch(arr, low, mid - 1, x)

    else:
        return bsearch(arr, mid + 1, high, x)


arr = [1, 3, 5, 7, 9, 11]

x = 7

ans = bsearch(arr, 0, len(arr)-1, x)

print("Answer =", ans)
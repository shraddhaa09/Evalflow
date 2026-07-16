def search(arr, item):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == item:
            return mid

        elif arr[mid] > item:
            high = mid - 1

        else:
            low = mid + 1

    return -1


a = [10, 20, 30, 40, 50]

ans = search(a, 30)

print(ans)
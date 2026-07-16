# binary search

arr = [1,3,5,7,9]

x = 7

low = 0
high = len(arr)-1

while low <= high:

    # middle position
    mid = (low + high)//2

    if arr[mid] == x:
        print("found")
        break

    elif arr[mid] < x:
        low = mid + 1

    else:
        high = mid - 1
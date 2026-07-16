arr = [2, 5, 8, 12, 16, 23, 38, 56]
x = 23

low = 0
high = len(arr) - 1

found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == x:
        print("Element found at position", mid)
        found = True
        break

    elif arr[mid] < x:
        low = mid + 1

    else:
        high = mid - 1

if found == False:
    print("Element not found")
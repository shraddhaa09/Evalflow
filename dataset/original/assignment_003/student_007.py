# binary search program

arr = [2,4,6,8,10,12]

# element to search
x = 10

low = 0
high = len(arr)-1

while low <= high:

    # finding middle
    mid = (low + high)//2

    # checking condition
    if arr[mid] == x:
        print("Found at", mid)
        break

    elif arr[mid] < x:
        low = mid + 1

    else:
        high = mid - 1
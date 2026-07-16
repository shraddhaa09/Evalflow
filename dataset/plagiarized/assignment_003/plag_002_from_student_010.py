arr = [2,4,6,8,10,12]

target = 8

l = 0
h = len(arr)-1

print("Searching...")

while l <= h:

    m = (l+h)//2

    print("Checking", arr[m])

    if arr[m] == target:
        print("Element found at", m)
        break

    elif arr[m] < target:
        l = m + 1

    else:
        h = m - 1
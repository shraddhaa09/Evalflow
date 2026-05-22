a = [5,10,15,20,25]

x = 20

low = 0
high = len(a)-1

print("Binary Search Begins")

while low <= high:

    mid = (low+high)//2

    print("Middle value:", a[mid])

    if a[mid] == x:
        print("Found")
        break

    elif a[mid] > x:
        high = mid - 1

    else:
        low = mid + 1
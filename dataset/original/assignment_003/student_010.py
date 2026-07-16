a = [3, 6, 9, 12, 15, 18]

search = 15

low = 0
high = len(a)-1

print("Starting Binary Search")

while low <= high:

    mid = (low + high)//2

    print("Checking middle element:", a[mid])

    if a[mid] == search:
        print("Element found")
        print("Index is", mid)
        break

    elif a[mid] > search:
        high = mid - 1

    else:
        low = mid + 1
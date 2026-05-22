# searching using binary search

a = [11,22,33,44,55]

search = 44

l = 0
h = len(a)-1

while l <= h:

    # calculate mid
    m = (l+h)//2

    if a[m] == search:
        print("Element Found")
        break

    elif search > a[m]:
        l = m + 1

    else:
        h = m - 1
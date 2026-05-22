n = int(input("Enter number of elements: "))

a = []

for i in range(n):
    val = int(input("Enter element: "))
    a.append(val)

key = int(input("Enter element to search: "))

l = 0
h = n - 1

while l <= h:

    m = (l + h) // 2

    if a[m] == key:
        print("Found")
        break

    if key > a[m]:
        l = m + 1
    else:
        h = m - 1

if l > h:
    print("Not Found")
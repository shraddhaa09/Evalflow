size = int(input("Enter size: "))

a = []

for i in range(size):
    x = int(input("Enter value: "))
    a.append(x)

key = int(input("Search value: "))

l = 0
h = size - 1

while l <= h:

    m = (l + h) // 2

    if key == a[m]:
        print("Found")
        break

    elif key > a[m]:
        l = m + 1

    else:
        h = m - 1

if l > h:
    print("Element absent")
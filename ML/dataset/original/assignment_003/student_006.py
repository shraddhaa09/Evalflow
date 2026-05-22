listt = [5, 9, 13, 27, 45, 60]

find = 27

first = 0
last = len(listt)-1

flag = 0

while first <= last:

    mid = (first + last)//2

    if listt[mid] == find:
        flag = 1
        break

    elif listt[mid] < find:
        first = mid + 1

    else:
        last = mid - 1

if flag == 1:
    print("Element found")
else:
    print("Element not found")
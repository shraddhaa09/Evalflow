p = int(input())

arr = []

for i in range(1, p + 1):
    if p % i == 0:
        arr.append(i)

if len(arr) == 2:
    print("Prime")
else:
    print("Not Prime")
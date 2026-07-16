x = int(input())

for i in range(2, x):
    if x % i == 0:
        print("No")
        break
else:
    if x > 1:
        print("Yes")
    else:
        print("No")
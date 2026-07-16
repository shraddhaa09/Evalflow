a = int(input())

flag = 1

if a <= 1:
    flag = 0
else:
    for j in range(2, a):
        if a % j == 0:
            flag = 0
            break

if flag == 1:
    print("Prime Number")
else:
    print("Not Prime Number")
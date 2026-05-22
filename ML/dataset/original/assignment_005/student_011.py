num = int(input())

if num < 2:
    print("Not Prime")

elif num == 2:
    print("Prime")

else:
    check = 0

    for i in range(2, num):
        if num % i == 0:
            check = 1

    if check == 0:
        print("Prime")
    else:
        print("Not Prime")
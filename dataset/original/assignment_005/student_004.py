x = int(input())

if x < 2:
    print("Not Prime")
else:
    f = True

    for k in range(2, x // 2 + 1):
        if x % k == 0:
            f = False

    if f:
        print("Prime")
    else:
        print("Not Prime")
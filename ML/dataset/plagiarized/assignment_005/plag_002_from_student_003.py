a = int(input())

k = 2

while k < a:
    if a % k == 0:
        print("Not Prime")
        break
    k = k + 1

else:
    if a > 1:
        print("Prime")
    else:
        print("Not Prime")
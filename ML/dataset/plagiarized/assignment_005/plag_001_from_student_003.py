num = int(input())

i = 2

while i < num:
    if num % i == 0:
        print("Not Prime")
        break
    i += 1

else:
    if num > 1:
        print("Prime")
    else:
        print("Not Prime")
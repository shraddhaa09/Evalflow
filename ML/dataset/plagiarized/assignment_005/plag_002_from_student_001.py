x = int(input())

factors = 0

for j in range(1, x + 1):
    if x % j == 0:
        factors = factors + 1

if factors == 2:
    print("Prime")
else:
    print("Not Prime")
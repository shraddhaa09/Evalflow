x = int(input())

c = 0

i = 1

while i <= x:
    if x % i == 0:
        c += 1
    i = i + 1

if c == 2:
    print("Prime Number")
else:
    print("Not Prime Number")
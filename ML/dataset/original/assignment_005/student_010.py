a = int(input())

s = 0

i = 1

while i <= a:
    if a % i == 0:
        s = s + 1
    i = i + 1

if s == 2:
    print("Prime Number")
else:
    print("Not Prime Number")
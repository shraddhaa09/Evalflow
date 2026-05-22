p = int(input())

d = []

for i in range(1, p + 1):
    if p % i == 0:
        d.append(i)

if len(d) == 2:
    print("Prime")
else:
    print("Not Prime")
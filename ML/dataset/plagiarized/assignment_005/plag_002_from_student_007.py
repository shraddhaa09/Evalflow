num = int(input())

f = []

for j in range(1, num + 1):
    if num % j == 0:
        f.append(j)

if len(f) == 2:
    print("Prime")
else:
    print("Not Prime")
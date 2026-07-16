n = int(input())

c = 0

for i in range(2, n):
    if n % i == 0:
        c += 1

if c > 0 or n <= 1:
    print("Composite")
else:
    print("Prime")
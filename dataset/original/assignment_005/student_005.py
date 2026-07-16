n = int(input())

temp = 0

for i in range(2, n):
    if n % i == 0:
        temp = temp + 1

if temp > 0 or n <= 1:
    print("Composite")
else:
    print("Prime")
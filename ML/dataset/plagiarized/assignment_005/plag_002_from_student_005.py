a = int(input())

temp = 0

for j in range(2, a):
    if a % j == 0:
        temp = temp + 1

if temp != 0 or a <= 1:
    print("Composite")
else:
    print("Prime")
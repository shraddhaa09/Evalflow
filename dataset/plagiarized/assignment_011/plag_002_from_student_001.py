num = int(input())

total = 0

while num > 0:
    r = num % 10
    total += r
    num //= 10

print(total)
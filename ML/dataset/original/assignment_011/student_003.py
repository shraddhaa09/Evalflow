a = int(input())

sum1 = 0

while a != 0:
    digit = a % 10
    sum1 += digit
    a //= 10

print("Sum =", sum1)
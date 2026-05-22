number = int(input())

s = 0

while number > 9:
    s = 0
    while number > 0:
        s += number % 10
        number = number // 10
    number = s

print(s)
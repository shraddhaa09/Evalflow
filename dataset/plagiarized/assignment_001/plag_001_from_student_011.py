n = int(input())

first = 0
second = 1

i = 1

while i <= n:

    print(first)

    sum = first + second
    first = second
    second = sum

    i = i + 1
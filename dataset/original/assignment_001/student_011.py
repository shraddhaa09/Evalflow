# fibonacci series program

n = int(input("Enter terms"))

first = 0
second = 1

i = 1

while i <= n:

    print(first)

    third = first + second
    first = second
    second = third

    i = i + 1
n = int(input("Enter a positive number: "))

if n <= 0:
    print("Invalid input")
else:
    a = 0
    b = 1

    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c
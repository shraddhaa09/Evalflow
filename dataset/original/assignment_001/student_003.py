def fibonacci(num):
    a = 0
    b = 1

    for i in range(num):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

n = int(input("Enter limit: "))
fibonacci(n)
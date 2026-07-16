n = int(input("Enter number: "))

a = 0
b = 1

print("Fibonacci Series")

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
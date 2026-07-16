n = int(input("Enter number"))

a = 0
b = 1

print(a)
print(b)

for i in range(2, n):
    d = a + b
    print(d)
    a = b
    b = d
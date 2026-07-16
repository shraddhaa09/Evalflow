num = int(input("Enter limit: "))

x = 0
y = 1

print(x)
print(y)

for i in range(2, num):
    z = x + y
    print(z)
    x = y
    y = z
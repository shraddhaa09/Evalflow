terms = int(input("Enter number"))

x, y = 0, 1

for i in range(terms):
    print(x, end=" ")
    x, y = y, x + y
n = int(input("How many terms"))

x = 0
y = 1
c = 0

while c < n:
    print(x)
    t = x + y
    x = y
    y = t
    c += 1
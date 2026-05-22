n = int(input("How many terms? "))

x = 0
y = 1
count = 0

while count < n:
    print(x)
    temp = x + y
    x = y
    y = temp
    count += 1
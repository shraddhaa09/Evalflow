terms = int(input())

a = 0
b = 1
count = 0

while count < terms:
    print(a)
    temp = a + b
    a = b
    b = temp
    count = count + 1
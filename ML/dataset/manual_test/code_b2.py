value = int(input("Input number: "))

count = len(str(value))

n = value
result = 0

while n != 0:
    rem = n % 10
    result += pow(rem, count)
    n = n // 10

if result == value:
    print("Armstrong")
else:
    print("Not Armstrong")
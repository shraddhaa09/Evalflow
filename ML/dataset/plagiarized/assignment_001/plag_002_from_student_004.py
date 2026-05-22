num = int(input("Enter terms"))

fib = [0,1]

for i in range(2, num):
    value = fib[i-1] + fib[i-2]
    fib.append(value)

print(fib)
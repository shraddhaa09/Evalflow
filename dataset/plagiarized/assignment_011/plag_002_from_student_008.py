def sumdigit(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sumdigit(n // 10)

n = int(input())

print(sumdigit(n))
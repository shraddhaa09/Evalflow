def digitsum(n):
    if n == 0:
        return 0
    return n % 10 + digitsum(n // 10)

n = int(input())

print(digitsum(n))
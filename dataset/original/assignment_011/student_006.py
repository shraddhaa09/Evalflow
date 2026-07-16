n = int(input())

temp = n
add = 0

while temp:
    add = add + temp % 10
    temp = temp // 10

print(add)
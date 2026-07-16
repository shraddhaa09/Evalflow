number = int(input())

prime = True

if number == 1 or number == 0:
    prime = False

for i in range(2, number):
    if number % i == 0:
        prime = False
        break

print(prime)
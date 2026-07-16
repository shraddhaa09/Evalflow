numbers = [12, 5, 8, 1, 19]

size = len(numbers)

for i in range(size):
    for j in range(size-1):
        if numbers[j] > numbers[j+1]:
            x = numbers[j]
            numbers[j] = numbers[j+1]
            numbers[j+1] = x

print(numbers)
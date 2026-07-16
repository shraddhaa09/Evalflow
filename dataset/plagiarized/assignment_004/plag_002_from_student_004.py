numbers = [10, 2, 15, 6, 4]

i = 0

while i < len(numbers):
    j = 0

    while j < len(numbers)-1:
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

        j = j + 1

    i = i + 1

print(numbers)
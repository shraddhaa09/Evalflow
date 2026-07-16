def split_numbers(data):
    evens = []
    odds = []

    for item in data:
        if item % 2 != 0:
            odds.append(item)
        else:
            evens.append(item)

    return evens, odds


values = [12, 7, 5, 18, 21, 30, 9, 4]

even_result, odd_result = split_numbers(values)

print("Even List:")
print(even_result)

print("Odd List:")
print(odd_result)
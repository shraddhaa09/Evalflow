def separate_even_odd(numbers):
    even_numbers = []
    odd_numbers = []

    for value in numbers:
        if value % 2 == 0:
            even_numbers.append(value)
        else:
            odd_numbers.append(value)

    return even_numbers, odd_numbers


nums = [12, 7, 5, 18, 21, 30, 9, 4]

even_list, odd_list = separate_even_odd(nums)

print("Even Numbers:")
print(even_list)

print("Odd Numbers:")
print(odd_list)
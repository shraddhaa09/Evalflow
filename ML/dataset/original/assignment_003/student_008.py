numbers = [14, 18, 21, 36, 40, 55]

target = 36

i = 0
j = len(numbers)-1

while i <= j:

    center = (i+j)//2

    if numbers[center] == target:
        print("Search successful")
        print(center)
        break

    elif target > numbers[center]:
        i = center + 1

    else:
        j = center - 1
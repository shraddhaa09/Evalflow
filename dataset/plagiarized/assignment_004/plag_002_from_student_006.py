data = [21, 11, 14, 3, 7]

for i in range(len(data)):
    swapped = False

    for j in range(len(data)-1-i):
        if data[j] > data[j+1]:
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp
            swapped = True

    if swapped == False:
        break

print(data)
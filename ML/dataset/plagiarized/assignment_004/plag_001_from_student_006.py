data = [21, 11, 14, 3, 7]

for pass1 in range(len(data)):
    swap = False

    for k in range(len(data)-1-pass1):
        if data[k] > data[k+1]:
            data[k], data[k+1] = data[k+1], data[k]
            swap = True

    if swap == False:
        break

print(data)
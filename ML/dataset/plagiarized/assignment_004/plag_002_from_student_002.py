a = [9, 7, 3, 1, 6]

for x in range(len(a)-1):
    for y in range(len(a)-1-x):
        if a[y] > a[y+1]:
            a[y], a[y+1] = a[y+1], a[y]

print("Sorted List :", a)
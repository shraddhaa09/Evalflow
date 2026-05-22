a = [9, 7, 3, 1, 6]

for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

print("Sorted List:", a)
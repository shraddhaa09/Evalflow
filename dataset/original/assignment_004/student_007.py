l = [44, 12, 9, 31, 5]

for i in range(1, len(l)):
    for j in range(len(l)-i):
        if l[j] > l[j+1]:
            temp = l[j+1]
            l[j+1] = l[j]
            l[j] = temp

print("After sorting")
print(l)
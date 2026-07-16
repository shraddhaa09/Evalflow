a=[12,45,7,89,23]
largest=a[0]

for i in range(len(a)):
    if a[i]>largest:
        largest=a[i]

print(largest)
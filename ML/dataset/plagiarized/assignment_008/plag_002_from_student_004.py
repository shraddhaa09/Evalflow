a=[]

for i in range(5):
    num=int(input())
    a.append(num)

largest=a[0]

for i in range(len(a)):
    if a[i]>largest:
        largest=a[i]

print("Largest number is",largest)
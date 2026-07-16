mylist = [90, 40, 70, 10]

n = len(mylist)

for i in range(n-1):
    for j in range(n-1):
        if mylist[j] > mylist[j+1]:
            temp = mylist[j]
            mylist[j] = mylist[j+1]
            mylist[j+1] = temp

print("Sorted elements are")
print(mylist)
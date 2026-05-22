list1 = [7,14,21,28,35]

num = 35

a = 0
b = len(list1)-1

while a<=b:

    c = (a+b)//2

    if num == list1[c]:
        print("yes found")
        break

    else:

        if num > list1[c]:
            a = c+1

        else:
            b = c-1
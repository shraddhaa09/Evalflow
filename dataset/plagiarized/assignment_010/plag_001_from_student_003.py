n=int(input())

flag=False

if n%4==0:
    if n%100==0:
        if n%400==0:
            flag=True
    else:
        flag=True

if flag==True:
    print("Yes")
else:
    print("No")
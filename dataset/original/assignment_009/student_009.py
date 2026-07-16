word=input("Enter word ")
temp=""
for i in word[::-1]:
    temp=temp+i
print(temp)
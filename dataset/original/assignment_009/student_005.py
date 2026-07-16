str1=input("Enter any string ")
ans=""
for i in range(len(str1)-1,-1,-1):
    ans=ans+str1[i]
print(ans)
s=input()
arr=[]

for i in s:
    arr.append(i)

ans=""

while arr:
    ans=ans+arr.pop()

print(ans)
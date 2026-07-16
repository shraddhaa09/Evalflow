text=input("Enter text ")
ans=""
i=len(text)-1

while(i>=0):
    ans=ans+text[i]
    i-=1

print(ans)
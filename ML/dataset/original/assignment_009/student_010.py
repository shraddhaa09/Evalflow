s=input()
stack=[]
for i in s:
    stack.append(i)

rev=""
while stack:
    rev=rev+stack.pop()

print(rev)
text=input("Enter string ")
stack=[]

for ch in text:
    stack.append(ch)

reverse=""

while len(stack)>0:
    reverse=reverse+stack.pop()

print(reverse)
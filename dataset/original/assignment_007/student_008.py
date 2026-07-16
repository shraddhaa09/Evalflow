s = input()

v = "aeiou"
ans = 0

for i in s:
    for j in v:
        if i.lower() == j:
            ans += 1

print(ans)
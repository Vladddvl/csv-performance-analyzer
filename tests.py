n = list(input())
flag = False
r = 0
l = 0
for i in range(len(n)):
    l = 0
    if n[i] == '(' and l <= r:
        r += 1
    elif n[i] == ')' and r >= l:
        l += 1
        r -= 1

if r == 0 and l == 1:
    flag = True

print(flag)

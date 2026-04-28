L = int(input())
R = int(input())

count = 0
for num in range(L, R + 1):
    s = str(num)
    valid = True
    for i in range(len(s) - 1):
        if s[i] <= s[i+1]:
            valid = False
            break
    if valid:
        count += 1

print(count)
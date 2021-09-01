s = input().split()
v = s.sort()
f = 0
s3 = ""
i = 0
j = len(s)
while i < j-1:
    i1 = i
    f = 0
    while s[i] == s[i1]:
        i1 += 1
        f += 1
        if i1 == j:
            break
        continue

    if f > 1:
        s3 = s3 + ' ' + str(s[i])
        if i1 == j:
            break
    i = i1
    continue
print(s3)
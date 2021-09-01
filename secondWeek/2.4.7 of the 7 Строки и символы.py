# put your python code here
s = input()
s3 = ""
i1 = 0
j = len(s)
while i1 < j:
    i2 = i1
    while s[i1] == s[i2]:
        i2 += 1
        if i2 == j:
            break
        continue
    s3 = s3 + s[i1] + str(i2-i1)
    i1 = i2
    continue
print(s3)





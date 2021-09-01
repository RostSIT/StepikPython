a = [int(i) for i in input().split()]
b = 0
z = ' 555'
j = 0
c = len(a)
while j > c:
    if len(a) == 1:
        print(a)
    if j == c[0]:
        z = z + str(c[1] + c[-1])
print(z)
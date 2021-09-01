
a = 'G17W12C2H5q13y2g16z19W14E2W20R9A17B7Y12a14F2w3T14g10A16g10u15J5f2u3p7x3'
b = []
for i in range(len(a)):
    if a[i].lower() in 'qwertyuiopasdfghjklzxcvbnm':
        b += a[i]
        a = a[:i] + "!" + a[i+1:]
c = a.split('!')[1:]
for i in range(len(b)):
    print(b[i] * int(c[i]), end="")

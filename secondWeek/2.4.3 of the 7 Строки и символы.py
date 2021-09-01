a = input()
d = a.lower()
dVarCounter = 0
b = 'c'
c = 'g'
i = 0
j = 0
for i in d:
    dVarCounter += 1
d.count(b)
d.count(c)
j = d.count(b) + d.count(c)
print(float(j) / float(dVarCounter) * 100)
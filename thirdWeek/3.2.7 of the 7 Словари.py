n = ''
n = str(input())
s = int(n)
c = {}
f = n * 2
i = 0

while i < s - 1:
    x = int(input())
    c[x] = f*(x)

    for value in c:
        print(value)
        

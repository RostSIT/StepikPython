a = int(input())
b = int(input())
c = 1
d = True
while d:
    if (c % a == 0) and (c % b == 0):
        print(c)
        break
    c += 1
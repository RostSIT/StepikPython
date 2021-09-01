# a, b = (int(i) for i in input().split()) - строка не проходит тест на stepik
a = int(input())
b = int(input())
c = 0
counter = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        c += i
        counter += 1
#        if c or d == 0:
#            continue
    continue
print(int(c) / int(counter))

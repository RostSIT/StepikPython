i = 0
while i <= 100:
    a = int(input())
    i = a
    if i > 100:
        break
    if i < 10:
        continue
    print(i)

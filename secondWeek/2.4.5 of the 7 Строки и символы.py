s = input()
i = 0
b = 0
for i in s:
    b += 1
print(str(s[3:6]), ' ' + str(s[:6]) + ' ' + str(s[3:]) + ' ' + str(s[::-1]) + ' ' + str(s[-3:]) + ' ' + str(s[:-6]) + ' ' + str(s[-1:-10:-2]))
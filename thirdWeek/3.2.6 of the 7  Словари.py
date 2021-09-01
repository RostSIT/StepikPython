myText = ''  # инициализация строки
myText = str(input())
lowerText = myText.lower()
myDict = {}  # инициализация пустого словаря

for wordInDict in lowerText.split():
    if wordInDict in myDict:
        myDict[wordInDict] += 1
    else:
        myDict[wordInDict] = 1

for key, value in myDict.items():
    print(key, value)





# m.append([str(s.lower()) for s in n.split()])
# li = len(m)
# lj = len(m[0])
# for i in range(li):
#     for j in range(lj):
#         p = m[i][j]
#         if p in d:
#             d[p] += 1
#         else:
#             d[p] = 1
# for key, value in d.items():
#     print(key, value)

# ccc cc cc c c c
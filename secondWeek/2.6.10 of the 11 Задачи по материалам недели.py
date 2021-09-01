# n, m = (int(i) for i in input().split())
# a = [[0 for j in range(m)] for i in range(n)]
# for i in range(n):
#     print(n, end=' ')
# for j in range(m):
#     print(m, end=' ')
# print(a)

n = ''
m = []
while True:
    n = str(input()) # ввод строк
    if n == 'end':
        break
    m.append([int(s) for s in n.split()])
li, lj = len(m), len(m[0])
new = [[sum([m[i-1][j], m[(i+1)%li][j], m[i][j-1], m[i][(j+1)%lj]]) for j in range(lj)] for i in range(li)]

for i in range (li):
    for j in range (lj):
        print(new[i][j], end =' ')
    print()

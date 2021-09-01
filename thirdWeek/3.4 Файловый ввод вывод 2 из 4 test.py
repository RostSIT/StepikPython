a = 'a3b4c2e10b1'
b = []
for i in range(len(a)):
    if a[i].lower() in 'qwertyuiopasdfghjklzxcvbnm':
        z = a[i+1:]
        x = a[:i]
        y = a[:i] + "!" + a[i+1:]
        b += a[i]
        a = a[:i] + "!" + a[i+1:]
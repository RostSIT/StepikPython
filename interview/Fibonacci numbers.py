lengthOfList = int(input())
fibonacciNumbers = []
a = range(lengthOfList)
firstNumberOnTheList, SecondNumberOnTheList = 0, 1
for i in a:
    if i == 0:
        fibonacciNumbers.append(firstNumberOnTheList)
    if i == 1:
        fibonacciNumbers.append(SecondNumberOnTheList)
    elif i > 1:
        theNextNumberInList = firstNumberOnTheList + SecondNumberOnTheList
        fibonacciNumbers.append(theNextNumberInList)
        firstNumberOnTheList = SecondNumberOnTheList
        SecondNumberOnTheList = theNextNumberInList
    i += 1
for i in fibonacciNumbers:
    print(i, end=' ')
print('- fibonacci numbers')


'''
f = int(input())
numberList = []
d = range(f)
i = 0
j = 0
a, b = 0, 1
for i in d:
    while j < i + 1:
        if j == 0:
            numberList.append(a)
        if j == 1:
            numberList.append(b)
        elif j > 1:
            c = a + b
            numberList.append(c)
            a = b
            b = c
        j += 1
print(numberList)
'''
'''numberList.append(i + 1)
        j += 1
    

print(numberList)

fibonacciNumbers = []

for n in numberList:
    def fib(n):
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a
    a = fib(n)
    fibonacciNumbers.append(a)


'''


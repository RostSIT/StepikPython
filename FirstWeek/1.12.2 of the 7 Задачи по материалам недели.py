# put your python code here

a = float(input())
b = float(input())
o = str(input())
if (b == 0 and o == '/') or (b == 0 and o == 'mod') or (b == 0 and o == 'div'):
    print('Деление на 0!')
else:
    if o == '+':
        print(a + b)
    if o == '-':
        print(a - b)
    if o == '/':
        print(a / b)
    if o == '*':
        print(a * b)
    if o == 'mod':
        print(a % b)
    if o == 'pow':
        print(a ** b)
    if o == 'div':
        print(a // b)

#   +, -, /, *, mod, pow, div,
#   mod — это взятие остатка от деления,
#   pow — возведение в степень,
#   div — целочисленное деление.

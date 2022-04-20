a = float(input("Введите число 1 "))
b = input("Введите знак +, -, *, /: ")
c = float(input("Введите число 2 "))
if b == '+':
    print(a+c)
elif b == '-':
    print(a-c)
elif b == '*':
    print(a * c)
elif c == 0 and b == '/':
    print("Делить на ноль нельзя")
elif b == '/':
    print(a / c)
b = 0
while b == 0:
    try:
        a = int(input("Введите число 1: "))
        b = int(input("Введите число 2: "))
        print("Результат деления:", a / b)
    except ValueError:
        print("Вводите только цифры")
    except ZeroDivisionError:
        print("Делить на ноль нельзя!")

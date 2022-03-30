import random

number = random.randint(1, 10)
color = random.randint(1, 2)
print(number, color)
tr = 1
# Номер попытки

# 1 - отвечает за красный цвет, 2 - за чёрный

while tr < 6:
    tr += 1
    user1 = int(input("Введите число от 1 до 10: "))
    user2 = int(input("Введите цвет: "))    # 1 - отвечает за красный цвет, 2 - за чёрный
    if user1 != number:
        print("Вы ввели неверное число")
        if user2 != color:
            print("Вы не угадали цвет")
        else:
            print("Вы угадали цвет")
    elif user1 != number:
        print("Вы ввели неверное число")
        if user2 == color:
            print("Вы угадали цвет")
        else:
            print("Вы не угадали цвет")
    elif user1 == number:
        print("Вы ввели верное число")
        if user2 == color:
            print("Вы угадали цвет")
        else:
            print("Вы не угадали цвет")
    elif user1 == number:
        print("Вы ввели верное число")
        if user2 != color:
            print("Вы не угадали цвет")
        else:
            print("Вы угадали цвет")
    elif user1 == number and user2 == color:
        print("Вы победили")
        break
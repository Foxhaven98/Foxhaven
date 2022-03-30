# Программа принимает на вход две строки и выводит в них общие буквы

stroka1 = input('Введите строку 1: ')
stroka2 = input('Введите строку 2: ')

mn1 = set(stroka1)
mn2 = set(stroka2)

print(mn1 & mn2)

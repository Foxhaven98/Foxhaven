a = input('Введите строку: ')
b = input('Введите символ: ')
c = ''
for i in a:
    if i != b:
        c = c+i
print('Результат: ', c)
import random

N = int(input('Введите количество элементов массива: '))
massiv = [int(input('Введите элемент массива: ')) for i in range(N)]

plus = 0
minus = 0

for i in range(N):
    if massiv[i] > 0:
        plus += 1
    elif massiv[i] < 0:
        minus += 1

if plus > minus:
    for i in range(minus, plus):
        massiv.append(random.randint(-100, -1))
elif plus < minus:
    for i in range(plus, minus):
        massiv.append(random.randint(1, 100))

print('Количество положительных элементов массива:', plus)
print('Количество отрицательных элементов массива:', minus)
print('Конечный массив:', massiv)

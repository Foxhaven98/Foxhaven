import math

x = float(input("Введите кординату x: "))
y = float(input("Введите кординату y: "))
r = float(input("Введите радиус круга: "))
# Найдём гипотенузу
h = math.sqrt(x**2 + y**2)

if h <= r:
    print("Точка принаджежит кругу")
else:
    print("Точка не принадлежит кругу")
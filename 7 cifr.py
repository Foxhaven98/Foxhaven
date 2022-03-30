import random

a = [random.randint(1, 10) for i in range(7)]
print(a)
count1 = 0
count2 = 0

# Находим количество чётных и нечётных цифр
for i in a:
    if i % 2 == 0:
        count1 += 1
    else:
        count2 += 1
print(f"Чётные: {count1}\nНечётные: {count2}")

# В зависимости от полученного результата выводим сумму или произведение
if count1 > count2:
    print("Сумма всех элементов =", sum(a))
else:
    print("Произведение 1, 3 и 6 элемента =", a[0] * a[2] * a[5])

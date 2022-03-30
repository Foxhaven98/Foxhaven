a = int(input("Введите число 1 "))
b = int(input("Введите число 2 "))
c = int(input("Введите число 3 "))

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print("Наибольшее", c)
    
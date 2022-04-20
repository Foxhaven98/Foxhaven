# выполняет только 1 операцию
# a = lambda x, y: x * y
# print(a(1, 2))

# def main(a):
#     def help(b):
#         return a * b
#     return help
# print(main(2)(3))
# two = main(2)
# print(two(4))

# def help(fn):
#     def wr(arg):
#         print("Start")
#         fn(arg)
#         print("Stop")
#     return wr
# @ help
# def fun1(arg):
#     print(arg**2)
# fun1(2)

# a = str(input())
# def fun(a):
#     return len(a)
# print(fun(a))

# a = int(input())
# def fun(a):
#     b = 0
#     while a % 10 >= 1:
#         a = a / 10
#         b += 1
#     return b
# print(fun(a))


# import math
#
# def kv(d):
#     Skv = d * d
#     return Skv
# def kr(r):
#     Skr = r * r * 3.14
#     return Skr
# def tr(a,b,c):
#     p = (a + b + c) / 2
#     Str = math.sqrt(p * (p - a) * (p - b) * (p - c))
#     return Str
# q = str(input("Площадь чего вы хотите найти? (Квадрат, Треугольник, Круг) "))
#
# if q == 'Квадрат':
#     print(kv(int(input("Введите сторону квадрата: "))))
# elif q == 'Круг':
#     print(kr(int(input("Введите радиус круга: "))))
# elif q == 'Треугольник':
#     print(tr(int(input("Введите сторону 1 треугольника: ")), int(input("Введите сторону 2 треугольника: ")), int(input("Введите сторону 3 треугольника: "))))

time = int(1234565)
day = time // 86400
hour = (time - (day * 3600 * 24)) // 3600
min = time - (day * 3600 * 24) - (hour * 60 * 60) // 60
sec = time - (day * 3600 * 24) - (hour * 60 * 60) // 60
print(min)
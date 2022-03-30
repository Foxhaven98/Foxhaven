# a = 'я,люблю,питон'
# b = (a.split(","))
# print(b)

# a = int(input("Введите число: "))
# b = ''
# while a > 0:
#     b = str(a % 2) + b
#     a = a // 2
# print(b)

# a = [1, 5, 0, 2, 7, 9]
# d = len(a)
# b = 0
# c = 0
# while c <= d:
#     if b in a:
#         a[a.index(b)], a[b] = a[b], a[a.index(b)]
#         b += 1
#     c += 1
# print(a)

# a = int(input('Введите число: '))
# b = 2
# while b in range(2, (a//2)+1):
#     if a % b != 0:
#         print("Число простое")
#         break
#     elif a % b == 0:
#         print("Число не простое")
#         break
#     b += 1

from random import randint

a = []
for i in range(10):
    a.append(randint(1, 50))
a.sort()
print(a)

k = int(input("Введите число: "))

mid = len(a) // 2
low = 0
high = len(a) - 1

while a[mid] != k and low <= high:
    if k > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("Значение отсутствует в списке")
else:
    print(mid)


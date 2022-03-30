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

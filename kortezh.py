# a = set([1, 2, 3, 4]) изменяемое множество
# a = frozenset([1, 2, 3, 4]) неизменяемое множество

# a = set([1, 2, 3, 4])
#
# print(5 in a)   Проверяет наличие

# a = set([1, 2, 3, 4])
# a.add(5)
# print(a) Добавляет элемент

# a = set([1, 2, 3, 4])
# a.discard(2) Удаляет
# a.remove(1)   Удаляет
# a.pop()   Удаляет первый элемент
# print(a)

# a = set([1, 2, 3, 4])
# a.clear()
# print(a)  Стирает всё

# a = {1, 2, 3, 4}
# b = {2, 8, 7, 6}
# a.union(b) тоже самое, что print(a|b)

# a = {1, 2, 3, 4}
# b = {2, 8, 7, 6}
# print(a & b)    Выводит повторяющиеся значения

# a = {1, 2, 3, 4}
# b = {2, 8, 7, 6}
# print(a-b) Выводит значения, которые есть в a, но нету в b

# a = {1, 2, 3, 4}
# b = {2, 8, 7, 6}
# x = a.isdisjoint(b)
# print(x)  Если есть пересечение между а и б, то False, иначе True

# a = {1, 2, 3, 4}
# print(len(a)) Выводит длину множества

a = {"строка": 'str', "кортеж": tuple('tup'), "список": [1, 3, 5], "число": int(8)}
print(dict.keys(a))
print(a["список"])
print(a.get())


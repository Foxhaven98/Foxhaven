a = [6, 4, 'py', 'tell', 78]
b = [44, 'hello', 56, 'exept', 3]
c = []

print("Сложение a и b: ", a + b)
a.insert(2, 6)
b.insert(2, 6)
print("Шестёрка на третьей позиции", a)
print("Шестёрка на третьей позиции", b)

a.remove('py')
a.remove('tell')
a.sort()
print(a)

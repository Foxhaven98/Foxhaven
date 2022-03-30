a = [1, 3, 9, 28, 8]
b = [2, 4, 8, 10, 11]
c = []

for i in a:
    if i in b:
        c.append(i)
print(c)
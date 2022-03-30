a = str(' Я  люблю Python ')
i = 0
while a[i] == ' ':
    i += 1
a = a[i:]
i = len(a)

while a[i - 1] == ' ':
    i -= 1
a = a[:i]
b = a[0]
i = 1
while i < len(a):
    if a[i] != ' ':
        b += a[i]
    elif a[i - 1] != ' ':
        b += '*'
    i += 1
print(b)

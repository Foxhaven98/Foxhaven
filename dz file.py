a = ('learn', 'i', 'python', '3', '10', '8')
b = []
c = []
for i in a:
    if i.isalpha():
        i = str(i)
        b.append(i)
    elif i.isdigit():
        i = int(i)
        c.append(i)
b.sort()
c.sort()
e = b + c
g = str(e)
f = open('dz.txt', 'w')
f.write(g)
f.close()

import random
a = []
m = 0
c = 0
for i in range(5):
    a.append([])
    for j in range(5):
        a[i].append(random.randint(1, 100))
        print(a[i][j], end=' ')
    print()
    if sum(a[i]) > m:
        m = (sum(a[i]))
        c = i+1
print(c, m)

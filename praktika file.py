# k = (10, 8, 29, 35, 7)
# a = -99999999999999999
# b = 999999999999999999
# for i in k:
#     if i > a:
#         a = i
#     if i < b:
#         b = i
# print('max =', a)
# print('min =', b)
# a, b = b, a
# print('max =', a)
# print('min =', b)

# a = str('pithonist')
# b = {i: a.count(i) for i in a}
# print(b)

# a = [0, 1, 0, 0, 1, 0, 0]
# b = 0
# c = 0
# for i in a:
#     if i == 0:
#         b += 1
#         if b == 2:
#             c += 1
#     else:
#         b = 0
# print(c)

# a = [7, -6, 10, 24, -36]
# plus = []
# minus = []
# for i in a:
#     if i > 0:
#         plus.append(i)
#     else:
#         minus.append(i)
# print(plus)
# print(minus)
#
# from random import random
# M = 5
# N = 5
# a = []
# b = []
# for i in range(M):
#     for j in range(N):
#         n = int(random() * 200)
#         b.append(n)
#         print('%4d' % n, end='')
#     a.append(b)
#     print()
# mx = -1
# for j in range(M):
#     mn = 200
#     for i in range(N):
#         if a[i][j] < mn:
#             mn = a[i][j]
#     if mn > mx:
#         mx = mn
# print("Максимальный среди минимальных: ", mx)

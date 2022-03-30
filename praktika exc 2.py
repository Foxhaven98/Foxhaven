# a = [1, 2, 3, 3, 4, 1]
# b = []
#
# for i in a:
#     if i not in b:
#         b.append(i)
#     elif i in b:
#         b.remove(i)
# print(b)
#
# a = [1, 2, 3, 3, 4, 1]
# b = list(set(a))
# print(len(a) - len(b))

a = [1, 2, 3, 3, 4, 1]
my_dict = {i: a.count(i) for i in a}
print(my_dict)

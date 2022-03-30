#f = open('text.txt', encoding='utf-8')
# # print(*f)   #открывает файл
# # print(f) #выводит тип
# f.close()
# with open('text.txt') as f:
#     print(f)
# print(f.read(7))  # выводит символы
# print(f.readlines())
# for i in f:
#     f.write('Hello')
# os.rename('new.txt', 'text.txt')
# print(os.getcwd())    местоположение файла
# os.mkdir('new')   создаёт папку
# os.chdir()    перемещает файл
# os.makedirs('...\...\...') создаёт вложенные папки
# os.remove('text.txt') Удаляет файл
# os.rmdir()    Удаляет папку (только пустую)
# os.removedirs('...\...\...') (удаляет все вложения папки)

# import re
#
# text = open('text.txt').read()
# summa = sum(map(int, re.findall(r'\d+', text)))
# print(summa)

f = open('text.txt')
a = f.readlines()
b = []
n = []
for i in a:
    i = i[:-1]
    if i.isalpha():
        i = str(i)
        b.append(i)
    elif i.isdigit():
        i = int(i)
        n.append(i)
print(b)
print(n)
b.sort()
n.sort()
e = b + n
print(e)



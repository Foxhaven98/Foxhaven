# list1 = [15,48,'hello',6,19,'world']
#
# vowels = "eyuioa"
#
# for i in enumerate(list1):
#     if i[1] is int:
#         if i[1] % 2 == 0:
#             sum1 = 0
#             for j in str(i[1]):
#                 sum1 += int(j)
#             print(sum1)
#         else:
#             list1[list1.index(i[1])] = 1
#     elif i[1] is str:
#         count_vowels = 0
#         count_consonants = 0
#         for j in i[1]:
#             if i[1] in vowels:
#                 count_vowels += 1
#             elif i[1].isalpha():
#                 count_consonants += 1
#         print(count_vowels)
#         print(count_consonants)



name = input("Введите имя: ")
while not name.isalpha():
    print("Некорректно введены данные, попробуй снова")
    name = input("Введите имя: ")
phone = input("Введите телефон: ")
while True:
    if "+" == phone[0] and "+375" == phone[:4] and len(phone) == 13:
        break
    else:
        print("Некорректно введены данные, попробуй снова")
        phone = input("Введите телефон: ")
email = input("Введите почту: ")
while True:
    if "@" in email and "." in email[email.index("@"):]:
        break
    else:
        print("Некорректно введены данные, попробуй снова")
        email = input("Введите почту: ")

catalog = ["Мяч", "Сетку", "Кроссовки"]
prices = [10, 20, 30]
categories = ["Обычный", "Спортивный", "Профессиональный"]
multiplicators = [1, 1.5, 2]

cart = []
while True:
    print("Добрый день, вас приветствует магазин спорт-товаров")
    print("1-Посмотреть каталог\n2-Выход из магазина")
    choice = input("Введите ваш выбор: ")
    if choice == "1":
        print("Каталог: ")
        for item in enumerate(catalog):
            print(f"{item[0]+1}-{item[1]}")
        choice_item = input("Выберите товар: ")
        print(f"Этот товар стоит: {prices[int(choice_item)-1]}")
        cart.append(int(choice_item)-1)
    if choice == "2":
        print("Корзина: ")
        sum1 = 0
        for i in cart:
            print(f"{catalog[i]} за {prices[i]}$")
            sum1 += prices[i]
        print(f"Итого: {sum1}")
        last_question = input("Будете брать? д/н ")
        if last_question == "д" or last_question == "да":
            print(f"Спасибо за покупку")
        else:
            print("Жаль, приходите ещё")
        exit("Всегда ждём вас в нашем магазине")









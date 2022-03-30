multik = {"обычный": 1, "спортивный": 2, "профессиональный": 3}

products = {"мяч": {"Количество": 3, "Стоимость": 10}, "сетка": {"Количество": 5, "Стоимость": 9}, "кроссовки": {"Количество": 7, "Стоимость": 8}}

cart = {
    "products":
            {
                "обычный": [],
                "спортивный": [],
                "профессиональный": []
            }

        }
#
# while True:
#     for product in products:
#         print(product.capitalize())
#     user_choice = input("Напиши название товара, который хочешь купить: ")
#     if user_choice.lower() in products:
#         print(f"Окей, вы выбрали {user_choice}\nСтоимость: {products[user_choice.lower()]}")
#         for mult in multik:
#             print(mult.capitalize())
#         user_choice_mult = input("Введите тип товара: ")
#         if user_choice_mult.lower() in multik:
#             cart["products"][user_choice_mult.lower()].append(user_choice.lower())
#             print("Товар добавлен в корзину.\nЧто-то ещё? (Д,Н):")
#             answer = input()
#             if "Н" in answer:
#                 break
#         else:
#             print("Нет такого варианта")
#     else:
#         print("Нет такого продукта")
# print(cart)

# Задание 1

# def fun(a):
#     return '*' * len(a[:-4]) + a[-4:]
# print(fun(input("Введите 16 цифр: ")))

# Задание 2

# def fun(a):
#     b = a[::-1]
#     if a == b:
#         return "Слово является палиндромом"
#     else:
#         return "Слово не является палиндромом"
# print(fun(input("Введите слово: ")))

# Задание 3

class Tomato:
    states = {1: 'Только посадили', 2: "Зелёный помидор", 3: "Созревший красный помидор"}

    def __init__(self, index):
        self._index = index
        self._state = 1

    def grow(self):
        if self._state < 3:
            self._state += 1
        return f'Tomato {self._index} is {Tomato.states[self._state]}'

    def is_ripe(self):
        if self._state == 3:
            return "Томат созрел"
        return "Томат ещё не созрел"

class TomatoBush:
    def __init__(self, a):
        self.tomatoes = [Tomato(index) for index in range(0, a)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print("Садовник работает")
        self._plant.grow_all()
        print("Работа завершена")

    def harvest(self):
        print("Садовник собирает урожай")
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Сбор завершён")
        else:
            print("Помидоры ещё зелёные, подожди")

    @staticmethod
    def knowledge_base():
        print("У помидора есть 3 статуса: когда его посадили, когда он начал расти и ещё зелёненький и когда он вырос и стал сочным \n"
              "красным помидором. Будь вниметел! Аккуратно ухаживай за садом и собирай помидоры только тогда, когда они созрели.")

Gardener.knowledge_base()
tomatobash = TomatoBush(4)
gardener = Gardener("Артём", tomatobash)
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
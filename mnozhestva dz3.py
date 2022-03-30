# Написать программу, которая отгадает число, которое пользователь загадал

min = 1
max = 100
while True:
    current = (min+max)//2
    is_max = input('Ваше число:{}?(да, больше, меньше)'.format(current))
    if is_max.lower() == 'да':
        print('Я его угадал!')
        break
    elif is_max=='больше':
        min = current + 1
    else:
        max = current - 1
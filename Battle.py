lastname = input("Введите фамилию: ")

if lastname == 'Stark':
    print('neutral')
elif lastname == 'Korstark' or lastname == 'Tully':
    print('friend')
else:
    print('enemy')

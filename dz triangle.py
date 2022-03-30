a = float(input("Введите длину стороны 1: "))
b = float(input("Введите длину стороны 2: "))
c = float(input("Введите длину стороны 3: "))

if a+b > c and a+c > b and b+c > a:
    if (a * a + b * b == c * c) or (a * a + c * c == b * b) or (b * b + c * c == a * a):
        print("Треугольник существует и он прямоугольный")
    elif (a * a + b * b > c * c) or (a * a + c * c > b * b) or (b * b + c * c > a * a):
        print("Треугольник существует и он острый")
    elif (a * a + b * b < c * c) or (a * a + c * c < b * b) or (b * b + c * c < a * a):
        print("Треугольник существует и он тупой")
else:
    print("Треугольник не существует")
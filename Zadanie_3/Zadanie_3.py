print("Определение типа треугольника по длинам сторон")

while True:
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    c = float(input("Введите длину стороны c: "))

    if a <= 0 or b <= 0 or c <= 0:
        print("\nОшибка: длины сторон должны быть положительными!")
    elif a + b <= c or a + c <= b or b + c <= a:
        print("\nОшибка: треугольник с такими сторонами не существует.")
    else:
        a2, b2, c2 = a*a, b*b, c*c

        cosA_num = b2 + c2 - a2
        cosB_num = a2 + c2 - b2
        cosC_num = a2 + b2 - c2

        if cosA_num == 0 or cosB_num == 0 or cosC_num == 0:
            print(f"\nТреугольник со сторонами ({a}; {b}; {c}) — ПРЯМОУГОЛЬНЫЙ.")
        elif cosA_num < 0 or cosB_num < 0 or cosC_num < 0:
            print(f"\nТреугольник со сторонами ({a}; {b}; {c}) — ТУПОУГОЛЬНЫЙ.")
        else:
            print(f"\nТреугольник со сторонами ({a}; {b}; {c}) — ОСТРОУГОЛЬНЫЙ.")
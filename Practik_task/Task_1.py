while True:
    rost = float(input("Введите ваш рост (см): "))
    ves = float(input("Введите ваш вес (кг): "))
    idealves = rost - 110
    print(f"Оптимальный вес: {idealves:.2f} кг")

    if abs(ves - idealves) <= 5:
        print("Ваш вес в норме")
    elif ves > idealves:
        print(f"Рекомендуется снизить вес до {idealves:.2f} кг")
    else:
        print(f"Рекомендуется набрать вес до {idealves:.2f} кг")
print("Программа вычисляет выражение:")
print("(a + b - f / a) + f * a * a - (a + b)\n")

a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
f = float(input("Введите число f: "))

result = (a + b - f / a) + f * a * a - (a + b)
print(f"\nРезультат: {result}")

if a == 0:
    print("Ошибка: деление на ноль (a не должно быть равно 0)")
else:
    result = (a + b - f / a) + f * a * a - (a + b)
    print(f"\nРезультат: {result}")
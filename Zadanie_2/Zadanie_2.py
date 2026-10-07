import math

print("Программа определяет, принадлежит ли точка заштрихованной области.")
print("Область ограничена: sin(x) <= y <= 0.5, π/6 <= x <= 5π/6\n")

while True:
    x = float(input("Введите координату x: "))
    y = float(input("Введите координату y: "))

    x_left  = math.pi / 6
    x_right = 5 * math.pi / 6
    y_bottom = 0.0
    y_top = 0.5

    if x_left <= x <= x_right and y_bottom <= y <= y_top:
        print(f"\nТочка ({x}; {y}) ПРИНАДЛЕЖИТ заштрихованной области.")
    else:
        print(f"\nТочка ({x}; {y}) НЕ принадлежит заштрихованной области.")
while True:
    nums = []
    for i in range(3):
        nums.append(float(input(f"Введите число {i+1}: ")))

    result = []
    for x in nums:
        if x == 1:
            result.append(2)
        elif x % 2 == 0:
            result.append(x / 2)
        else:
            result.append(x)

    print("Результат:", result)
def find_password(n):
    result = ""

    # Подбираем все уникальные пары
    pairs = []
    for i in range(1, n):          # Первое число пары
        for j in range(i + 1, n + 1):  # Второе число пары
            pairs.append((i, j))   # Добавляем пару в список

    # Проверяем кратность заданного числа
    for a, b in pairs:
        pair_sum = a + b
        if n % pair_sum == 0:      # Если n кратно сумме пары
            result += f"{a}{b}"     # Добавляем пару к результату

    return result

# Тестирируем для n от 3 до 20
for i in range(3, 21):
    print(f"{i} - {find_password(i)}")

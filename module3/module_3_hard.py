def calculate_structure_sum(data):
    total_sum = 0

    for item in data:
        if isinstance(item, (int, float)):  # Если элемент - число
            total_sum += item
        elif isinstance(item, str):  # Если элемент - строка
            total_sum += len(item)
        elif isinstance(item, dict):  # Если элемент - словарь
            for key, value in item.items():
                total_sum += calculate_structure_sum([key, value])  # Рекурсивный вызов на ключи и значения
        elif isinstance(item, (list, tuple)):  # Если элемент - список или кортеж
            total_sum += calculate_structure_sum(item)  # Рекурсивный вызов на вложенные структуры

    return total_sum


# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Вывод: 99

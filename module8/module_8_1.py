def add_everything_up(a, b):
    # Проверяем, являются ли a и b числом
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    # Если один - это строка, а другой - число
    elif isinstance(a, str) and isinstance(b, (int, float)):
        return a + str(b)
    elif isinstance(b, str) and isinstance(a, (int, float)):
        return str(a) + b
    # Если a и b разные типы (число и строка), возвращаем их строковое представление
    elif (isinstance(a, (int, float)) and isinstance(b, str)) or (isinstance(a, str) and isinstance(b, (int, float))):
        return str(a) + str(b)
    else:
        raise TypeError("Неизвестный тип данных.")

# Примеры использования
print(add_everything_up(123.456, 'строка'))  # 123.456строка
print(add_everything_up('яблоко', 4215))     # яблоко4215
print(add_everything_up(123.456, 7))          # 130.456

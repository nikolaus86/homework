def get_multiplied_digits(number):
    str_number = str(number)  # Преобразуем число в строку
    first = int(str_number[0])  # Берем первый символ и преобразуем в число

    # Если длина строки больше 1, продолжаем вычисления
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))

    # Если оставшаяся длина равна 1, возвращаем первую цифру
    return first
result = get_multiplied_digits(40203)
print(result)
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Список длин строк из first_strings, длина которых не менее 5 символов
first_result = [len(word) for word in first_strings if len(word) >= 5]

# Список пар слов (кортежей) одинаковой длины
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

# Словарь, где парой ключ-значение будет строка-длина строки (чётная длина)
third_result = {word: len(word) for word in first_strings + second_strings if len(word) % 2 == 0}

# Выводим результаты
print(first_result)
print(second_result)
print(third_result)

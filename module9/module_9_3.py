first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для разницы длин строк
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

# Генераторная сборка для сравнения длин строк
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Печать результатов
print(list(first_result))
print(list(second_result))

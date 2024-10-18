def single_root_words(root_word, *other_words):
    # Приводим базовое слово к нижнему регистру для сравнения
    root_word_lower = root_word.lower()
    same_words = []

    # Перебираем каждое слово из списка other_words
    for word in other_words:
        # Приводим текущее слово к нижнему регистру
        word_lower = word.lower()
        # Проверяем наличие root_word в текущем слове или наоборот
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

    return same_words

# Примеры вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

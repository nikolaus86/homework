def single_root_words(root_word, *other_words):
    same_words = []  # Создаем пустой список для результатов

    # Перебираем все слова из other_words
    for word in other_words:
        # Проверяем, содержится ли root_word в слове или слово в root_word
        if root_word in word or word in root_word:
            same_words.append(word)  # Добавляем слово в список

    return same_words  # Возвращаем список подходящих слов
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
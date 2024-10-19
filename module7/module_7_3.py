import re

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    words = []
                    for line in file:
                        # Приводим строку к нижнему регистру
                        line = line.lower()
                        # Убираем пунктуацию (используем регулярные выражения)
                        line = re.sub(r'[^\w\s]', '', line)
                        # Разбиваем строку на слова
                        words.extend(line.split())
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
        return all_words

    def find(self, word):
        result = {}
        word = word.lower()
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1  # 1-based index
        return result

    def count(self, word):
        result = {}
        word = word.lower()
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            count = words.count(word)
            if count > 0:
                result[file_name] = count
        return result

# Пример использования
finder = WordsFinder('test_file.txt')
print(finder.get_all_words())  # Все слова
print(finder.find('TEXT'))      # Позиция первого вхождения
print(finder.count('teXT'))     # Количество вхождений

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

finder2 = WordsFinder('Rudyard Kipling - If.txt',)

print(finder2.get_all_words())
print(finder2.find('if'))
print(finder2.count('if'))


finder3 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder3.get_all_words())
print(finder3.find('captain'))
print(finder3.count('captain'))
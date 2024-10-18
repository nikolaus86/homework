import string


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
                        # Приводим строку к нижнему регистру и удаляем пунктуацию
                        line = line.lower().translate(str.maketrans('', '', string.punctuation + " -"))
                        words.extend(line.split())
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл '{file_name}' не найден.")
        return all_words

    def find(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                results[file_name] = words.index(word) + 1  # Позиция +1 для 1-индексирования
        return results

    def count(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            results[file_name] = words.count(word)
        return results


# Пример использования
if __name__ == "__main__":
    finder = WordsFinder('test_file.txt')

    print("Все слова в файлах:")
    print(finder.get_all_words())  # Получить все слова

    print("\nПозиция слова 'TEXT':")
    print(finder.find('TEXT'))  # Найти позицию слова

    print("\nКоличество вхождений слова 'teXT':")
    print(finder.count('teXT'))  # Подсчитать количество вхождений слова

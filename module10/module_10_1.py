import threading
from time import sleep, time

# Функция для записи слов в файл
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")  # Запись слова в файл
            sleep(0.1)  # Пауза в 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")

# Измерение времени выполнения функций
start_time = time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time()
print(f"Работа функций {end_time - start_time:.6f} секунд")

# Измерение времени выполнения потоков
start_time_threads = time()

# Создание потоков для записи
threads = []
thread_args = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt'),
]

for args in thread_args:
    t = threading.Thread(target=write_words, args=args)
    threads.append(t)
    t.start()

# Ожидание завершения всех потоков
for t in threads:
    t.join()

end_time_threads = time()
print(f"Работа потоков {end_time_threads - start_time_threads:.6f} секунд")

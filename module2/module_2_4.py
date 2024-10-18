numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for num in numbers:
    if num <= 1:
        continue  # Пропускаем числа 0 и 1
    is_prime = True  # Предполагаем, что число простое
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            is_prime = False  # Нашли делитель, значит число не простое
            break  # Прекращаем проверку, так как знаем, что число составное
    if is_prime:
        primes.append(num)  # Добавляем простое число в список
    else:
        not_primes.append(num)  # Добавляем составное число в список

# Выводим результаты
print("Primes:", primes)
print("Not Primes:", not_primes)

import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0  # начальный баланс
        self.lock = threading.Lock()  # объект Lock

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # случайная сумма пополнения
            with self.lock:  # блокировка для безопасного доступа к баланс
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")

                # Если баланс >= 500 и lock заблокирован, разблокируем его
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()

            time.sleep(0.001)  # имитация задержки

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)  # случайная сумма снятия
            print(f"Запрос на {amount}")

            with self.lock:  # блокировка для проверки и изменения баланса
                if amount <= self.balance:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    self.lock.acquire()  # блокируем поток, т.к. недостаточно средств


if __name__ == "__main__":
    bk = Bank()

    # Создаем два потока для методов deposit и take
    th1 = threading.Thread(target=Bank.deposit, args=(bk,))
    th2 = threading.Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')

import threading
import time
import random


class Bank (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.balance = 0
        self.lock = threading.Lock()


    def deposit(self):
        for transaction in range(100):
            random_sum = random.randint(50,500)
            if self.balance >=500 and self.lock.locked():
                self.lock.release()
            self.balance += random_sum
            print(f'Пополнение: {random_sum}. Баланс: {self.balance}')
            time.sleep(0.001)



    def take(self):
        for transaction in range(100):
            random_sum = random.randint(50, 500)
            print(f'Запрос на {random_sum}')
            if random_sum <= self.balance:
                self.balance -= random_sum
                print(f'Снятие: {random_sum}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
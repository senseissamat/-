import datetime
import os
from abc import ABC, abstractmethod

# ------------------ ТАПСЫРМА 1 ------------------
class Transport(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def energy_source(self):
        pass


class Auto(Transport):
    def drive(self):
        return "-> Auto: Жолда тез қозғалады."

    def energy_source(self):
        return "-> Auto: Бензин немесе дизель қолданады."


class Bike(Transport):
    def drive(self):
        return "-> Bike: Веложолда баяу қозғалады."

    def energy_source(self):
        return "-> Bike: Адам күші арқылы қозғалады."


def task1():
    print("--- ТАПСЫРМА 1: TRANSPORT АБСТРАКЦИЯСЫ ---")
    car = Auto()
    bike = Bike()

    print(f"\n[Auto]: {car.drive()}")
    print(f"[Auto]: {car.energy_source()}")

    print(f"\n[Bike]: {bike.drive()}")
    print(f"[Bike]: {bike.energy_source()}")
    print("-" * 50)


# ------------------ ТАПСЫРМА 2 ------------------
class DBConnector(ABC):
    @abstractmethod
    def open(self): pass

    @abstractmethod
    def close(self): pass

    @abstractmethod
    def query(self, sql): pass


class MySQL(DBConnector):
    def open(self):
        print("-> MySQL: Қосылу сәтті (порт 3306).")

    def close(self):
        print("-> MySQL: Қосылым жабылды.")

    def query(self, sql):
        print(f"-> MySQL: Сұрау орындалды: '{sql}'")


class Postgres(DBConnector):
    def open(self):
        print("-> Postgres: Қосылу сәтті (порт 5432).")

    def close(self):
        print("-> Postgres: Байланыс тоқтатылды.")

    def query(self, sql):
        print(f"-> Postgres: Сұрау орындалды: '{sql}'")


def task2():
    print("--- ТАПСЫРМА 2: DATABASE ИНТЕРФЕЙС ---")
    db = MySQL()
    db.open()
    db.query("SELECT * FROM employees;")
    db.close()
    print("-" * 50)


# ------------------ ТАПСЫРМА 3 ------------------
class BaseLogger(ABC):
    def _decorate(self, msg: str) -> str:
        now = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        return f"{now} - {msg}"

    @abstractmethod
    def write(self, msg: str):
        pass


class ConsoleLog(BaseLogger):
    def write(self, msg: str):
        formatted = self._decorate(f"[INFO] {msg}")
        print(f"Консоль: {formatted}")


class FileLog(BaseLogger):
    def __init__(self, filename="system_log.txt"):
        self.filename = filename
        # Очистим файл при создании
        if os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8") as f:
                f.write("")

    def write(self, msg: str):
        formatted = self._decorate(f"[FILE] {msg}")
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(formatted + "\n")
        print(f"Файлға жазылды: {msg}")


def task3():
    print("--- ТАПСЫРМА 3: LOGGER ---")
    console = ConsoleLog()
    file = FileLog()

    console.write("Жүйе іске қосылды.")
    file.write("Қате: 500 Internal Server Error.")

    print(f"\n[{file.filename} мазмұны]:")
    try:
        with open(file.filename, "r", encoding="utf-8") as f:
            print(f.read().strip())
    except FileNotFoundError:
        print("Файл табылмады.")
    print("-" * 50)


# ------------------ ТАПСЫРМА 4 ------------------
class Plane(Transport):
    def drive(self):
        return "-> Plane: Әуеде ұшады."

    def energy_source(self):
        return "-> Plane: Авиациялық отын пайдаланады."


class Railway(Transport):
    def drive(self):
        return "-> Railway: Рельстермен қозғалады."

    def energy_source(self):
        return "-> Railway: Электр немесе дизель қолданады."


def task4():
    print("--- ТАПСЫРМА 4: ПОЛИМОРФИЗМ ---")
    transports = [Auto(), Bike(), Plane(), Railway()]
    for t in transports:
        print(f"{t.__class__.__name__}: {t.drive()}")
    print("-" * 50)


# ------------------ ТАПСЫРМА 5 ------------------
class PaymentGateway(ABC):
    @abstractmethod
    def authorize(self, amount): pass

    @abstractmethod
    def pay(self, amount): pass

    @abstractmethod
    def rollback(self, txn_id): pass


class PayPalSystem(PaymentGateway):
    def authorize(self, amount):
        print(f"-> PayPal: {amount} KZT үшін авторизация.")

    def pay(self, amount):
        print(f"-> PayPal: {amount} KZT төлемі жасалды.")

    def rollback(self, txn_id):
        print(f"-> PayPal: {txn_id} транзакциясы қайтарылды.")


class KaspiSystem(PaymentGateway):
    def authorize(self, amount):
        print(f"-> Kaspi: {amount} KZT үшін QR арқылы авторизация.")

    def pay(self, amount):
        print(f"-> Kaspi: {amount} KZT төлемі орындалды.")

    def rollback(self, txn_id):
        print(f"-> Kaspi: {txn_id} транзакциясы бойынша қайтару сұралды.")


def task5():
    print("--- ТАПСЫРМА 5: PAYMENT SYSTEM ---")
    paypal = PayPalSystem()
    kaspi = KaspiSystem()

    amount = 7500
    txn_id = "TXN_123456"

    print("\n[PayPal]:")
    paypal.authorize(amount)
    paypal.pay(amount)
    paypal.rollback(txn_id)

    print("\n[Kaspi]:")
    kaspi.authorize(amount)
    kaspi.pay(amount)
    kaspi.rollback(txn_id)

    print("-" * 50)


# ------------------ MAIN ------------------
if __name__ == "__main__":
    task1()
    print("\n")
    task2()
    print("\n")
    task3()
    print("\n")
    task4()
    print("\n")
    task5()
[19:11, 14.12.2025] Ахи💩: import threading
from datetime import datetime

# -----------------------
# Task 1: Singleton Logger
# -----------------------
class Logger:
    _instance = None
    _lock = threading.Lock()  # for thread safety

    def _new_(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls.instance = super().new_(cls)
                    cls._instance.logs = []
        return cls._instance

    def log(self, message):
        timestamped = f"{datetime.now()} - {message}"
        self.logs.append(timestamped)
        return timestamped

# -----------------------
# Task 2: Strategy Pattern for Discounts
# -----------------------
class DiscountStrategy:
    def apply(self, price):
        raise NotImplementedError()

class NoDiscount(DiscountStrategy):
    def apply(self, price):
        return price

class PercentageDiscount(DiscountStrategy):
    def _init_(self, percent):
        self.percent = percent

    def apply(self, price):
        return price * (1 - self.percent / 100)

class FixedDiscount(DiscountStrategy):
    def _init_(self, amount):
        self.amount = amount

    def apply(self, price):
        return max(0, price - self.amount)

def calculate_total(price, strategy: DiscountStrategy):
    return strategy.apply(price)

# -----------------------
# Task 3: Factory Pattern for Notifications
# -----------------------
class Notification:
    def send(self, message):
        raise NotImplementedError()

class EmailNotification(Notification):
    def send(self, message):
        print(f"Email sent: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"SMS sent: {message}")

class PushNotification(Notification):
    def send(self, message):
        print(f"Push Notification sent: {message}")

class NotificationFactory:
    _types = {
        "email": EmailNotification,
        "sms": SMSNotification,
        "push": PushNotification
    }

    @classmethod
    def get(cls, channel: str):
        if channel in cls._types:
            return cls._types[channel]()
        else:
            raise ValueError(f"Unknown channel: {channel}")

# -----------------------
# Task 4: Observer Pattern
# -----------------------
class Subject:
    def _init_(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        raise NotImplementedError()

class ConsoleSubscriber(Observer):
    def update(self, message):
        print(f"ConsoleSubscriber received: {message}")

class FileSubscriber(Observer):
    def update(self, message):
        # Simulating writing to file
        print(f"FileSubscriber received: {message} (would be saved to file)")

# -----------------------
# Task 5: Integrated Event Logging System
# -----------------------
class EventLogger(Subject):
    def _init_(self):
        super()._init_()
        self.logger = Logger()  # Singleton Logger

    def log_event(self, message):
        log_msg = self.logger.log(message)
        self.notify(log_msg)

# -----------------------
# Demonstration (run directly)
# -----------------------

# Task 1: Singleton Test
logger1 = Logger()
logger2 = Logger()
logger1.log("System started")
print("Logger singleton test:", logger1 is logger2)
print(logger2.logs)
print()

# Task 2: Strategy Test
price = 200
no_discount = NoDiscount()
perc_discount = PercentageDiscount(10)
fixed_discount = FixedDiscount(30)

print("Original price:", price)
print("No discount:", calculate_total(price, no_discount))
print("10% discount:", calculate_total(price, perc_discount))
print("Fixed 30 discount:", calculate_total(price, fixed_discount))
print()

# Task 3: Factory Test
factory = NotificationFactory()
factory.get("email").send("Hello via Email!")
factory.get("sms").send("Hello via SMS!")
factory.get("push").send("Hello via Push!")
print()

# Task 4 & 5: Observer + Singleton Integration
event_logger = EventLogger()
console_sub = ConsoleSubscriber()
file_sub = FileSubscriber()

event_logger.attach(console_sub)
event_logger.attach(file_sub)

event_logger.log_event("User logged in")
event_logger.log_event("Error occurred")
[19:12, 14.12.2025] Ахи💩: Нау 15
[19:12, 14.12.2025] Ахи💩: class Robot:
    def _init_(self, model, power):
        self._model = model
        self._power = power

    @property
    def power(self):
        return self._power


    @power.setter
    def power(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Қуат деңгейі 0 мен 100 арасында болуы керек!")
        self._power = value


    def work(self):
        if self._power <= 10:
            print(f"{self._model}: Қуат аз! Заряд керек ⚡️")
        else:
            self._power -= 10
            print(f"{self._model} жұмыс істеді. Қалған қуат: {self._power}%")


    def charge(self, amount):
        self._power = min(100, self._power + amount)
        print(f"{self._model} қуатталды! Қазір қуаты: {self._power}%")



class AdvancedRobot(Robot):

    def boost_power(self, percent):
        self.power += self.power * percent
        if self.power > 100:
            self.power = 100
        print(f"{self._model} қуаты boost арқылы артты! Қуаты: {self.power}%")



bot1 = Robot("Atlas", 50)
print("Бастапқы қуат:", bot1.power)
bot1.work()
bot1.charge(30)
print("Қазіргі қуат:", bot1.power)

print("\n--- AdvancedRobot ---")
bot2 = AdvancedRobot("T-800", 70)
bot2.boost_power(0.2)
bot2.work()
bot2.charge(15)
print("Соңғы қуат:", bot2.power)
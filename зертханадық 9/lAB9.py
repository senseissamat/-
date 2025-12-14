class Robot:
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
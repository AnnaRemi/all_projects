from abc import ABC, abstractmethod


class MagicUnit(ABC):
    health = 100
    damage = None
    speed = None
    protection = None
    price = None
    energy = 100

    def info_health(self):
        return self.health

    def info_protection(self):
        return self.protection

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def treat(self):
        pass

    @abstractmethod
    def shield(self):
        pass

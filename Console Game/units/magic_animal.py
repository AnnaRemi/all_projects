from abc import abstractmethod
from units.magic_unit import MagicUnit


class MagicAnimal(MagicUnit):
    speed = 10
    protection = 30
    price = 15

    @abstractmethod
    def treat(self):
        pass

    def attack(self):
        pass

    @abstractmethod
    def shield(self):
        pass

from abc import abstractmethod
from units.magic_unit import MagicUnit


class MagicAnimal(MagicUnit):
    def __init__(self):
        super().__init__()
        self._speed = 10
        self._protection = 30
        self._price = 15
        self._weapon = 'claws'
        self._damage = 0

    def treat(self):
        return True

    def attack(self):
        return 0

    def shield(self):
        return True

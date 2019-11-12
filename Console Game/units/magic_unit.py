from abc import ABC, abstractmethod


class MagicUnit(ABC):
    def __init__(self):
        self._health = 100
        self._damage = None
        self._speed = None
        self._protection = None
        self._price = None
        self.name = None

    def get_name(self):
        return self._name

    @abstractmethod
    def treat(self):
        pass

    @abstractmethod
    def shield(self):
        pass

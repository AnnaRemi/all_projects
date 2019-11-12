from abc import ABC, abstractmethod


class ElementFactory(ABC):
    _money = 100
    price = {'girl': 30, 'boy': 30, 'animal': 15}

    def can_create_magic_unit(self, unit):
        try:
            if self._money >= self.price[unit]:
                self._money -= self.price[unit]
                return True
            return False
        except KeyError:
            return None

    @abstractmethod
    def create_magic_girl(self):
        pass

    @abstractmethod
    def create_magic_boy(self):
        pass

    @abstractmethod
    def create_magic_animal(self):
        pass

    def return_message(self):
        return 'You have {} coins'.format(self._money)

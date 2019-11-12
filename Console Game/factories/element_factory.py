from abc import ABC, abstractmethod


class ElementFactory(ABC):
    money = 100

    def can_create_magic_unit(self, price, creating_unit):
        if self.money >= price:
            self.money -= price
            return creating_unit()
        return "You don't have enough coins, please write" \
               " Q to change element or choose another element"

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
        return 'You have {} coins'.format(self.money)

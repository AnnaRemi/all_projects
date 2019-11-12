from factories.element_factory import ElementFactory
from units.magic_girl import MagicGirl
from units.magic_boy import MagicBoy
from units.magic_animal import MagicAnimal


class FireElementFactory(ElementFactory):
    def create_magic_girl(self):
        return FireMagicGirl()

    def create_magic_boy(self):
        return FireMagicBoy()

    def create_magic_animal(self):
        return FireMagicAnimal()


class FireMagicGirl(MagicGirl):
    def __init__(self):
        super().__init__()
        self._weapon = 'fffire!'


class FireMagicBoy(MagicBoy):
    def __init__(self):
        super().__init__()
        self._weapon = 'torch'


class FireMagicAnimal(MagicAnimal):
    def __init__(self):
        super().__init__()

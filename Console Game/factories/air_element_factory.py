from factories.element_factory import ElementFactory
from units.magic_girl import MagicGirl
from units.magic_boy import MagicBoy
from units.magic_animal import MagicAnimal


class AirElementFactory(ElementFactory):
    def create_magic_girl(self):
        return AirMagicGirl()

    def create_magic_boy(self):
        return AirMagicBoy()

    def create_magic_animal(self):
        return AirMagicAnimal()


class AirMagicGirl(MagicGirl):
    def __init__(self):
        self._weapon = 'huuuuricane!'


class AirMagicBoy(MagicBoy):
    def __init__(self):
        super().__init__()
        self._weapon = 'air sword'


class AirMagicAnimal(MagicAnimal):
    def __init__(self):
        super().__init__()

from factories.element_factory import ElementFactory
from units.magic_girl import MagicGirl
from units.magic_boy import MagicBoy
from units.magic_animal import MagicAnimal


class WaterElementFactory(ElementFactory):
    def create_magic_girl(self):
        return WaterMagicGirl()

    def create_magic_boy(self):
        return WaterMagicBoy()

    def create_magic_animal(self):
        return WaterMagicAnimal()


class WaterMagicGirl(MagicGirl):
    def __init__(self):
        super().__init__()
        self._weapon = 'flooood!'


class WaterMagicBoy(MagicBoy):
    def __init__(self):
        super().__init__()
        self._weapon = 'sharp knife'


class WaterMagicAnimal(MagicAnimal):
    def __init__(self):
        super().__init__()

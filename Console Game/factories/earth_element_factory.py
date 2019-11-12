from factories.element_factory import ElementFactory
from units.magic_girl import MagicGirl
from units.magic_boy import MagicBoy
from units.magic_animal import MagicAnimal


class EarthElementFactory(ElementFactory):
    def create_magic_girl(self):
        return EarthMagicGirl()

    def create_magic_boy(self):
        return EarthMagicBoy()

    def create_magic_animal(self):
        return EarthMagicAnimal()


class EarthMagicGirl(MagicGirl):
    def __init__(self):
        super().__init__()
        self._weapon = 'ssswamp!'


class EarthMagicBoy(MagicBoy):
    def __init__(self):
        super().__init__()
        self._weapon = 'wooden nunchuck'


class EarthMagicAnimal(MagicAnimal):
    def __init__(self):
        super().__init__()

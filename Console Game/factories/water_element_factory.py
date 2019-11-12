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
    spell = 'flooood!'


class WaterMagicBoy(MagicBoy):
    weapon = 'sharp knife'


class WaterMagicAnimal(MagicAnimal):

    def treat(self):
        WaterMagicBoy.health += 5
        WaterMagicGirl.health += 5
        WaterMagicAnimal.health += 5
        return 'Treatment Water Army!'

    def shield(self):
        WaterMagicBoy.protection += 1
        WaterMagicGirl.protection += 1
        WaterMagicAnimal.protection += 1
        return 'Protect Water Army!'

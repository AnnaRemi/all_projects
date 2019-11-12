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
    spell = 'fffire!'


class FireMagicBoy(MagicBoy):
    weapon = 'torch'


class FireMagicAnimal(MagicAnimal):

    def treat(self):
        FireMagicBoy.health += 5
        FireMagicGirl.health += 5
        FireMagicAnimal.health += 5
        return "Treatment Fire Army!"

    def shield(self):
        FireMagicBoy.protection += 1
        FireMagicGirl.protection += 1
        FireMagicAnimal.protection += 1
        return 'Protect Air Army!'

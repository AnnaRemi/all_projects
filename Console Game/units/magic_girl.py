from units.magic_unit import MagicUnit


class MagicGirl(MagicUnit):
    damage = 25
    speed = 20
    spell = None
    protection = 5
    price = 30

    def attack(self):
        print('Attack on {}'.format(self.spell))
        self.energy -= 5
        return [self.damage, self.spell]

    def treat(self):
        pass

    def shield(self):
        pass

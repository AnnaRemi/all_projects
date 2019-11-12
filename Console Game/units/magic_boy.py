from units.magic_unit import MagicUnit


class MagicBoy(MagicUnit):
    damage = 15
    speed = 15
    weapon = 'none'
    spell = None
    protection = 20
    price = 30

    def attack(self):
        print('Attack on {}'.format(self.weapon))
        self.energy -= 3
        return [self.damage, self.spell]

    def treat(self):
        pass

    def shield(self):
        pass

from abc import ABC, abstractmethod
from units.magic_unit import MagicUnit
from structure.component import Component


class Proxy(Component):
    def __init__(self, real_subject: Component):
        self._real_subject = real_subject

    def info_health(self):
        print('{} : health is {}'.format(self._real_subject.name, self._real_subject.info_health()))

    def damage(self, loss):
        print('Opponent attacked on {}'.format(self._real_subject.name))
        return self._real_subject.damage(loss)

    def treat(self):
        if self._real_subject.check_treat():
            print('{} recuperated'.format(self._real_subject.name))
        else:
            print("{} : sorry, army can't treat yourself".format(self._real_subject.name))

    def attack(self):
        print('{} attack!!'.format(self._real_subject.name))
        return self._real_subject.attack()

    def die(self):
        died_units = self._real_subject.die()
        if died_units is None:
            print('{} is died. GAME OVER!'.format(self._real_subject.name))
        for unit in died_units:
            print('{} is died'.format(unit))

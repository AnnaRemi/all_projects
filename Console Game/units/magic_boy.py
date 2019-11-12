from units.magic_unit import MagicUnit


class MagicBoy(MagicUnit):
    def __init__(self):
        super().__init__()
        self._damage = 15
        self._speed = 15
        self._weapon = None
        self._protection = 20
        self._price = 30

    def treat(self):
        return False

    def shield(self):
        return False

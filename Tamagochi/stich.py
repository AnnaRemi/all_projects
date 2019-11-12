from pet import Pet
from design import STICH_IMAGES


class Stich(Pet):
    def __init__(self, pict_s=STICH_IMAGES.STICH_HELLO, pict_die=STICH_IMAGES.STICH_DIE,
                 pict_funny=STICH_IMAGES.STICH_FUNNY, pict_eat=STICH_IMAGES.STICH_EAT,
                 pict_left=STICH_IMAGES.STICH_LEFT, pict_right=STICH_IMAGES.STICH_RIGHT,
                 pict_sleep=STICH_IMAGES.STICH_SLEEP, pict_angry=STICH_IMAGES.STICH_ANGRY,
                 pict_upset=STICH_IMAGES.STICH_UPSET, pict_happy=STICH_IMAGES.STICH_HAPPY):
        Pet.__init__(self,  5, 20, 20, 100, 0.5, 500, pict_s, pict_die, pict_funny, pict_eat, pict_left, pict_right, pict_sleep,
                     pict_angry, pict_upset, pict_happy)

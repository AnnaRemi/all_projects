from pet import Pet
from design import CAT_IMAGES


class Cat(Pet):
    def __init__(self, pict_s=CAT_IMAGES.CAT_HELLO, pict_die=CAT_IMAGES.CAT_DIE, pict_funny=CAT_IMAGES.CAT_FUNNY,
                 pict_eat=CAT_IMAGES.CAT_EAT, pict_left=CAT_IMAGES.CAT_LEFT,
                 pict_right=CAT_IMAGES.CAT_RIGHT, pict_sleep=CAT_IMAGES.CAT_SLEEP,
                 pict_angry=CAT_IMAGES.CAT_ANGRY, pict_upset=CAT_IMAGES.CAT_UPSET, pict_happy=CAT_IMAGES.CAT_HAPPY):
        Pet.__init__(self,  4, 20, 30, 50, 1, 100, pict_s, pict_die, pict_funny, pict_eat, pict_left, pict_right, pict_sleep, pict_angry,
                     pict_upset, pict_happy)


from pet import Pet
from design import FOX_IMAGES


class Fox(Pet):
    def __init__(self, pict_s=FOX_IMAGES.FOX_HELLO, pict_die=FOX_IMAGES.FOX_DIE, pict_funny=FOX_IMAGES.FOX_FUNNY,
                 pict_eat=FOX_IMAGES.FOX_EAT, pict_left=FOX_IMAGES.FOX_LEFT,
                 pict_right=FOX_IMAGES.FOX_RIGHT, pict_sleep=FOX_IMAGES.FOX_SLEEP, pict_angry=FOX_IMAGES.FOX_ANGRY,
                 pict_upset=FOX_IMAGES.FOX_UPSET, pict_happy=FOX_IMAGES.FOX_HAPPY):
        Pet.__init__(self, 5, 10, 30, 30, 1, 50, pict_s, pict_die, pict_funny, pict_eat, pict_left, pict_right,
                     pict_sleep, pict_angry, pict_upset, pict_happy)

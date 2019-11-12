import pygame
from pygame import *


class DISPLAY(object):
    """Display specifications"""
    COLOR_OF_DISPLAY = "bisque"
    COLOR_BLACK = "black"
    COLOR_WHITE = "white"
    HEIGHT_SCREEN = 800
    WIDTH_SCREEN = 600
    STAY_X = HEIGHT_SCREEN // 2
    STAY_Y = WIDTH_SCREEN // 2 + 80
    RADIUS = 60
    SIZE_OF_PET = 120


class CAT_IMAGES(object):
    """Pictures for cat conditions"""
    CAT_HELLO = 'images/cat_hello.png'
    CAT = 'images/cat.png'
    CAT_DIE = 'images/cat_die.png'
    CAT_FUNNY = 'images/cat_funny.png'
    CAT_EAT = 'images/cat_eat.png'
    CAT_LEFT = 'images/cat_left.png'
    CAT_RIGHT = 'images/cat_right.png'
    CAT_SLEEP = 'images/cat_sleep.png'
    CAT_ANGRY = 'images/cat_angry.png'
    CAT_UPSET = 'images/cat_upset.png'
    CAT_HAPPY = 'images/cat_happy.png'


class FOX_IMAGES(object):
    """Pictures for fox conditions"""
    FOX_HELLO = 'images/fox_hello.png'
    FOX = 'images/fox.png'
    FOX_DIE = 'images/fox_die.png'
    FOX_FUNNY = 'images/fox_funny.png'
    FOX_EAT = 'images/fox_eat.png'
    FOX_LEFT = 'images/fox_left.png'
    FOX_RIGHT = 'images/fox_right.png'
    FOX_SLEEP = 'images/fox_sleep.png'
    FOX_ANGRY = 'images/fox_angry.png'
    FOX_UPSET = 'images/fox_upset.png'
    FOX_HAPPY = 'images/fox_happy.png'


class STICH_IMAGES(object):
    """Pictures for stich conditions"""
    STICH_HELLO = 'images/stich_hello.png'
    STICH = 'images/stich.png'
    STICH_DIE = 'images/stich_die.png'
    STICH_FUNNY = 'images/stich_funny.png'
    STICH_EAT = 'images/stich_eat.png'
    STICH_LEFT = 'images/stich_left.png'
    STICH_RIGHT = 'images/stich_right.png'
    STICH_SLEEP = 'images/stich_sleep.png'
    STICH_ANGRY = 'images/stich_angry.png'
    STICH_UPSET = 'images/stich_upset.png'
    STICH_HAPPY = 'images/stich_happy.png'


class Background(object):
    """Creating background for the room in which the pet lives"""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((DISPLAY.HEIGHT_SCREEN, DISPLAY.WIDTH_SCREEN))
        pygame.display.set_caption("YOUR THE BEST PET EVER")
        self.background = pygame.image.load('images/pet_bg.png')
        self.background = pygame.transform.scale(self.background, (800, 600))

        self.food = pygame.image.load('images/feed_n.png').convert_alpha()
        self.food = pygame.transform.scale(self.food, (3 * DISPLAY.SIZE_OF_PET // 4, 3 * DISPLAY.SIZE_OF_PET // 4))
        self.food_place = self.food.get_rect(centerx=270, centery=(DISPLAY.SIZE_OF_PET * 2 - 120) // 2 + 10)

        self.sleep = pygame.image.load('images/sleep.png').convert_alpha()
        self.sleep = pygame.transform.scale(self.sleep, (DISPLAY.SIZE_OF_PET - 30, DISPLAY.SIZE_OF_PET - 30))
        self.sleep_place = self.sleep.get_rect(centerx=270 + DISPLAY.SIZE_OF_PET,
                                               centery=(DISPLAY.SIZE_OF_PET * 2 - 120) // 2 + 10)







from cat import Cat
from fox import Fox
from stich import Stich
from design import DISPLAY
import pygame
from pygame import *

def create_pets(game_screen, *args):
    """The first screen where user chooses the kind of pet.
    Arguments are pet picture.
    Return list of pet pictures.
    """
    create_place = pygame.image.load('images/choose_a_pet_bg.png')
    create_place = pygame.transform.scale(create_place, (DISPLAY.HEIGHT_SCREEN, DISPLAY.WIDTH_SCREEN))
    game_screen.screen.blit(create_place, (0, 0))
    length = 0
    pets = []
    for picture in args:
        pet_image = pygame.image.load(picture)
        pet_image = pygame.transform.scale(pet_image, (DISPLAY.SIZE_OF_PET * 2, DISPLAY.SIZE_OF_PET * 2))
        pet_image_r = pet_image.get_rect(center=(DISPLAY.SIZE_OF_PET + length, DISPLAY.SIZE_OF_PET + 40 + 100))
        game_screen.screen.blit(pet_image, pet_image_r)
        length += DISPLAY.SIZE_OF_PET * 2
        pets.append(pet_image_r)
    pygame.display.update()
    return pets


def choose_pet(pets):
    """Choice of a particular pet.
    Argument is list of pet picture.
    Return specific pet that user chose.
    """
    check_create = True
    while check_create:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if pets[0].collidepoint(event.pos) and pygame.mouse.get_pressed()[0]:
                    newpet_ = Cat()
                elif pets[1].collidepoint(event.pos) and pygame.mouse.get_pressed()[0]:
                    newpet_ = Fox()
                elif pets[2].collidepoint(event.pos) and pygame.mouse.get_pressed()[0]:
                    newpet_ = Stich()
                check_create = False
    return newpet_

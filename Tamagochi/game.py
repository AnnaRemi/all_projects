from creating import create_pets, choose_pet

import pygame
from pygame import *

from design import Background, CAT_IMAGES, FOX_IMAGES, STICH_IMAGES


class Game(object):
    def __init__(self):
        """Creating a screen where user can choose a pet"""
        self.game_screen = Background()
        self.check_mouse = True
        self.check_die = False
        self.check_create = True
        pets = create_pets(self.game_screen, CAT_IMAGES.CAT, FOX_IMAGES.FOX, STICH_IMAGES.STICH)
        self.newpet = choose_pet(pets)
        self.check_not_die = True
        self.check_moving = 'none'
        self.check_play = False
        self.check_sleep = False

    def run(self):
        """The main game loop"""
        while True:
            pygame.display.update()
            if self.check_not_die:
                self.game_screen.screen.blit(self.game_screen.background, (0, 0))
                self.game_screen.screen.blit(self.game_screen.food, self.game_screen.food_place)
                self.game_screen.screen.blit(self.game_screen.sleep, self.game_screen.sleep_place)
                self.newpet.message()
                self.newpet.stay(self.game_screen)
                self.newpet.info(self.game_screen)
            self.newpet.become_hungry()
            self.newpet.become_upset()
            self.newpet.become_grown()
            self.newpet.become_rested()
            self.newpet.move()
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                if self.check_not_die:
                    self.check_play = self.newpet.play(event)
                    self.check_mouse = self.newpet.feed(self.game_screen, event, self.check_mouse)
                    self.check_sleep = self.newpet.sleep(self.game_screen, event, self.check_sleep)
                    self.newpet.move_start_or_finish(event)
                    pygame.display.update()
            self.check_not_die = self.newpet.die(self.game_screen)
            pygame.display.update()
        quit()


if __name__ == "__main__":
    Game().run()


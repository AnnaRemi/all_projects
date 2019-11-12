from design import Background, DISPLAY

import pygame
from pygame import *
import time


class Pet(object):
    """Creating some attributes about pet condition"""
    location_x = DISPLAY.STAY_X
    location_y = DISPLAY.STAY_Y
    radius_of_pet = DISPLAY.RADIUS
    hunger = 29
    mood = 70
    energy = 100
    SIZE_OF_PET = 120
    ENERGY_PERIOD_WITH_MOTION = 0.3
    ENERGY_PERIOD_SLEEP = 1
    hunger_time = time.time()
    mood_time = time.time()
    energy_time = time.time()
    energy_time_with_motion = 0
    speed_of_rested = 1
    die = False
    check_want_to_sleep = 0
    funny_time = 0
    age = 0
    now_sleep = False
    age_time = time.time()
    images = {}
    mood_state = 'stay'
    state = 'stay'
    feed_time = time.time()
    right = False
    left = False

    def __init__(self, hunger_period, mood_period, energy_period, age_period, funny_period, max_age, pict_s, pict_die,
                 pict_funny, pict_eat, pict_left, pict_right, pict_sleep, pict_angry, pict_upset, pict_happy):
        """Creating the dictionary with pet views in concrete state and short names of states.
        Arguments are picture's ways in fields (type string).
        """
        new_image = self.create_pict(pict_s, 'stay')
        self.images.update(new_image)
        new_image = self.create_pict(pict_die, 'die')
        self.images.update(new_image)
        new_image = self.create_pict(pict_funny, 'funny')
        self.images.update(new_image)
        new_image = self.create_pict(pict_eat, 'eat')
        self.images.update(new_image)
        new_image = self.create_pict(pict_left, 'left')
        self.images.update(new_image)
        new_image = self.create_pict(pict_right, 'right')
        self.images.update(new_image)
        new_image = self.create_pict(pict_sleep, 'sleep')
        self.images.update(new_image)
        new_image = self.create_pict(pict_angry, 'angry')
        self.images.update(new_image)
        new_image = self.create_pict(pict_upset, 'upset')
        self.images.update(new_image)
        new_image = self.create_pict(pict_happy, 'happy')
        self.images.update(new_image)
        self.mood_period = mood_period
        self.hunger_period = hunger_period
        self.energy_period = energy_period
        self.age_period = age_period
        self.funny_period = funny_period
        self.energy_period_now = self.energy_period
        self.MAX_AGE = max_age

    def create_pict(self, pict_s, arg):
        """Create new picture.
        Arguments are pict_s (picture's way in fields, type string) and arg
        (short name of picture's value, type string)..
        Return the pair of short name and transformed picture.
        """
        pet_i = pygame.image.load(pict_s).convert_alpha()
        pet_i = pygame.transform.scale(pet_i, (self.SIZE_OF_PET * 2, self.SIZE_OF_PET * 2))
        return {arg: pet_i}

    def feed(self, game_screen, event, check):
        """Depending on the event feeds the pet.
        Arguments are event and check (it's true if mouse isn't pressed, type bool).
        Return true if mouse isn't pressed, else return false.
        """
        if not self.now_sleep and pygame.mouse.get_pressed()[0]:
            want_to_feed = False
            if game_screen.food_place.collidepoint(event.pos):
                want_to_feed = True
            if want_to_feed and check:
                if self.hunger < 100:
                    self.hunger += 5
                    if self.hunger > 100:
                        self.hunger = 100
                    self.state = 'eat'
                    self.feed_time = time.time()
        return not pygame.mouse.get_pressed()[0]

    def sleep(self, game_screen, event, check):
        """If needed button is pressed, pet sleeps. To wake up need to press this button again.
        Arguments are event and check (it's true if mouse isn't pressed, type bool).
        Return true if mouse isn't pressed, else return false.
        """
        if pygame.mouse.get_pressed()[0]:
            want_to_sleep = False
            if game_screen.sleep_place.collidepoint(event.pos):
                want_to_sleep = True
            if want_to_sleep and check:
                if self.check_want_to_sleep == 0:
                    if self.energy < 100:
                        self.state = 'sleep'
                        self.energy_period_now = self.ENERGY_PERIOD_SLEEP
                        self.check_want_to_sleep = 1
                        self.now_sleep = True
                else:
                    self.energy_period_now = self.energy_period
                    self.state = self.mood_state
                    self.check_want_to_sleep = 0
                    self.now_sleep = False
        return not pygame.mouse.get_pressed()[0]

    def info(self, game_screen):
        """Display the information about pet's states"""
        place = pygame.font.Font(None, 36)
        hunger = place.render('Сытость : {}'.format(self.hunger), 1, Color(DISPLAY.COLOR_BLACK))
        game_screen.screen.blit(hunger, (10, 10))
        mood_ = place.render('Настроение : {}'.format(self.mood), 1, Color(DISPLAY.COLOR_BLACK))
        game_screen.screen.blit(mood_, (10, 46))
        energy_ = place.render('Энергия : {}'.format(self.energy), 1, Color(DISPLAY.COLOR_BLACK))
        game_screen.screen.blit(energy_, (10, 82))
        age = place.render('Возраст : {}'.format(self.age), 1, Color(DISPLAY.COLOR_BLACK))
        game_screen.screen.blit(age, (10, 118))
        pygame.display.update()

    def move_start_or_finish(self, event):
        """Mpves the pet when the button is pressed for a long time and stops the pet when button isn't pressed.
         Argument is current event.
         """
        if not self.now_sleep and self.energy > 0:
            if self.left or event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.location_x -= 1
                self.left = True
                self.state = 'left'
            if self.right or event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.location_x += 1
                self.right = True
                self.state = 'right'
            if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                self.left = False
                if not self.right:
                    self.state = self.mood_state
                else:
                    self.state = 'right'
            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                self.right = False
                if not self.left:
                    self.state = self.mood_state
                else:
                    self.state = 'left'

    def move(self):
        """Moves the pet when the button is pressed for a first time"""
        if self.energy > 0:
            if self.left:
                self.location_x -= 2
            if self.right:
                self.location_x += 2
            if self.location_x >= DISPLAY.HEIGHT_SCREEN + self.radius_of_pet:
                self.location_x = 0
            if self.location_x < -1 * self.radius_of_pet:
                self.location_x = DISPLAY.HEIGHT_SCREEN
            if self.left or self.right:
                if self.energy_time_with_motion == 0:
                    self.energy_time_with_motion = time.time()
                else:
                    if time.time() - self.energy_time_with_motion > self.ENERGY_PERIOD_WITH_MOTION:
                        self.energy -= 1
                        self.energy_time_with_motion = time.time()

    def stay(self, game_screen):
        """Drawing pet in current state and upgrade the screen"""
        if self.state == 'eat':
            if time.time() - self.feed_time > 0.5:
                self.state = self.mood_state
        if self.state == 'stay':
            self.state = self.mood_state
        game_screen.screen.blit(self.images[self.state],
                               (self.location_x - self.SIZE_OF_PET, self.location_y - self.SIZE_OF_PET))

    def become_hungry(self):
        """Reduces the hunger balance"""
        if time.time() - self.hunger_time > self.hunger_period and self.hunger > 0:
            self.hunger -= 1
            self.hunger_time = time.time()

    def become_rested(self):
        """Increases the energy balance"""
        if self.energy == 100 and self.now_sleep == 1:
            self.state = self.mood_state
            self.now_sleep = False
            self.energy_period_now = self.energy_period
        if time.time() - self.energy_time > self.energy_period_now and self.energy < 100:
            self.energy += 1
            self.energy_time = time.time()

    def become_upset(self):
        """Reduces the mood balance"""
        if time.time() - self.mood_time > self.mood_period and self.mood > 0:
            self.mood -= 1
            self.mood_time = time.time()

    def become_grown(self):
        """Increases the age balance"""
        if time.time() - self.age_time > self.age_period and self.age < self.MAX_AGE:
            self.age += 1
            self.age_time = time.time()

    def die(self, game_screen):
        """Pet dies if hunger or mood balance equals zero or age balance equals 100.
        Return true if pet doesn't die.
        """
        if self.hunger == 0 or self.age == self.MAX_AGE or self.mood == 0:
            die_place = pygame.Surface((DISPLAY.HEIGHT_SCREEN, DISPLAY.WIDTH_SCREEN))
            die = pygame.font.Font(None, 25)
            a = 'тебя не было слишком долго.'
            die = die.render(a, 1, Color(DISPLAY.COLOR_WHITE))
            die_place.blit(die, (DISPLAY.HEIGHT_SCREEN // 2 - len(a) * 4,
                                 DISPLAY.WIDTH_SCREEN // 2 - 4*self.radius_of_pet))
            game_screen.screen.blit(die_place, (0, 0))
            game_screen.screen.blit(self.images['die'], (DISPLAY.HEIGHT_SCREEN // 2 - self.SIZE_OF_PET,
                                                        DISPLAY.WIDTH_SCREEN // 2 - self.SIZE_OF_PET))
            pygame.display.update()
            return False
        else:
            return True

    def become_funny(self):
        """Increases the mood balance"""
        if time.time() - self.funny_time > self.funny_period and self.mood < 100:
            self.mood += 1
            self.funny_time = time.time()

    def play(self, event):
        """Changing pet condition and view when the mouse inside the pet"""
        if not self.now_sleep and (self.state == self.mood_state or self.state == 'funny'):
            if event.type == pygame.MOUSEMOTION:
                pet_i_r = self.images[self.state].get_rect(centerx=self.location_x, centery=self.location_y)
                if pet_i_r.collidepoint(event.pos):
                    if pygame.mouse.get_rel()[0] != 0:
                        self.become_funny()
                        self.state = 'funny'
                else:
                    self.state = self.mood_state

    def message(self):
        """Changing pet view during of its balance"""
        if self.hunger > 70 and self.mood > 70:
            self.mood_state = 'happy'
        else:
            if self.hunger < 30:
                self.mood_state = 'angry'
            elif self.mood_state == 'angry' or self.mood_state == 'happy':
                self.mood_state = 'stay'
            if self.mood < 30:
                self.mood_state = 'upset'
            elif self.mood_state == 'upset' or self.mood_state == 'happy':
                self.mood_state = 'stay'

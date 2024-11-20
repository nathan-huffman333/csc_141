# For comments see alien_invasion.py

import pygame
from pygame.sprite import Sprite
from random import randint

class Raindrop(Sprite):
    """A class to represent a single raindrop in the rainfieldt."""

    def __init__(self, ri_game):
        super().__init__()
        self.screen = ri_game.screen
        self.settings = ri_game.settings

        # Load the raindrop image and set its rect attribute.
        self.image = pygame.image.load('13_aliens/13_03_raindrops/raindrop.png')
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the raindrop's exact horizontal position.
        self.y = float(self.rect.y)

        self.speed = randint(6, 10)

    def update(self):
        """Move the raindrop down."""
        self.y += self.speed
        self.rect.y = self.y
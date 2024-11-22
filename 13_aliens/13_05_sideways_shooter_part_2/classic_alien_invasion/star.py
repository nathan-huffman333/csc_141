# For comments see alien_invasion.py

import pygame
from pygame.sprite import Sprite
from random import randint

class Star(Sprite):
    """A class to represent a single star in the background."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # Load the star image and set its rect attribute.
        self.image = pygame.image.load('alien_invasion_sprites/star.png')
        self.rect = self.image.get_rect()


        # Start each new star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the star's exact horizontal position.
        self.y = float(self.rect.y)

        self.speed = randint(6, 10)

    def update(self):
        """Move the raindrop down."""
        self.y += self.speed
        self.rect.y = self.y
# For comments, see alien_invasion.py

import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('12_a_ship_that_fires_bullets/12_02_game_character/spaceship.png')
        self.rect = self.image.get_rect()

        # self.rect.midbottom = self.screen_rect.midbottom
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
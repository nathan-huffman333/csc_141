# For comments, see rain_invasion.py

import pygame

class Cloud:
    """A class to manage the cloud."""

    def __init__(self, ri_game):
        """Initialize the ship and set its starting position."""
        self.screen = ri_game.screen
        self.screen_rect = ri_game.screen.get_rect()

        # Load the cloud image and get its rect.
        self.image = pygame.image.load('13_aliens/13_04_steady_rain/cloud.png')
        self.rect = self.image.get_rect()

        self.rect.midtop = self.screen_rect.midtop

    def blitme(self):
        """Draw the cloud at its current location."""
        self.screen.blit(self.image, self.rect)
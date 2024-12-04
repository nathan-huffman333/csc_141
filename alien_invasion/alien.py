import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game, alien_type = 1):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.alien_type = alien_type

        # Load the alien image and set its rect attribute.
        if self.alien_type == 1:
            self.image = pygame.image.load('alien_invasion/alien_invasion_sprites/alien1.png')
        elif self.alien_type == 2:
            self.image = pygame.image.load('alien_invasion/alien_invasion_sprites/alien2.png')
        elif self.alien_type == 3:
            self.image = pygame.image.load('alien_invasion/alien_invasion_sprites/alien3.png')

        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
    

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)


    def update(self):
        """Move the alien left or right."""

        """
        if self.alien_type == 1:
            self.x += self.settings.alien_speed * self.settings.fleet_direction
        elif self.alien_type == 2:
            self.x += self.settings.alien_speed * self.settings.fleet_direction
        elif self.alien_type == 3:
            self.x += self.settings.alien_speed * self.settings.fleet_direction
        """
        
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
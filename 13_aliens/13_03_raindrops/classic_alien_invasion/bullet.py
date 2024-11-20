# For comments see alien_invasion.py

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""
    def __init__(self, ai_game, offset=11):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect1 = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect1.topleft = ai_game.ship.rect.topleft
        self.rect1.x += offset
        self.rect1.y += offset


        self.rect2 = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect2.topright = ai_game.ship.rect.topright
        self.rect2.x -= offset
        self.rect2.y += offset

        # Store the bullet's position as a float.
        self.y1 = float(self.rect1.y)
        self.y2 = float(self.rect2.y)

        self.x1 = float(self.rect1.x)
        self.x2 = float(self.rect2.x)
    

    def update(self):
        """Move the bullet up the screen."""
        # Update the exact position of the bullet.
        self.y1 -= self.settings.bullet_speed
        self.y2 -= self.settings.bullet_speed

        if self.x1 != self.x2:
            self.x1 += self.settings.bullet_merge
            self.x2 -= self.settings.bullet_merge
        else:
            self.rect1 = pygame.Rect(0, 0, self.settings.bullet_width*2, self.settings.bullet_height+10)
            self.rect2 = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height+10)
        # Update the rect position.
        self.rect1.y = self.y1
        self.rect2.y = self.y2

        self.rect1.x = self.x1
        self.rect2.x = self.x2


    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect1)
        pygame.draw.rect(self.screen, self.color, self.rect2)
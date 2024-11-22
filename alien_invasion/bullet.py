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
        # Update the exact position of the bullets.
        self.y1 -= self.settings.bullet_speed
        self.y2 -= self.settings.bullet_speed

        if abs(self.x1 - self.x2) > self.settings.merge_threshold:  # Smooth merging condition
            # Lasers are moving inward toward each other
            self.x1 += self.settings.bullet_merge_speed
            self.x2 -= self.settings.bullet_merge_speed
        else:
            # Once close enough, merge into a single beam
            self.rect1.width = self.settings.bullet_width * 2
            self.rect1.x = (self.x1 + self.x2) / 2 - self.rect1.width / 2
            self.rect2 = None  # Remove the second rect once merged

        self.rect1.y = self.y1
        self.rect1.x = self.x1

        if self.rect2:  # Only update rect2 if it exists
            self.rect2.y = self.y2
            self.rect2.x = self.x2
        else:
            # After merging, ensure the beam moves only vertically
            self.rect1.x = self.x1

 

    
    def draw_bullet(self):
        """Draw the bullet(s) to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect1) 
        if self.rect2:
            pygame.draw.rect(self.screen, self.color, self.rect2)



    @property    
    def rect(self):
        """Return a bounding rect that encompasses both rect1 and rect2."""
        if self.rect2:
            left = min(self.rect1.left, self.rect2.left)
            right = max(self.rect1.right, self.rect2.right)
            top = min(self.rect1.top, self.rect2.top)
            bottom = max(self.rect1.bottom, self.rect2.bottom)
            return pygame.Rect(left, top, right - left, bottom - top)
        else:
            return self.rect1
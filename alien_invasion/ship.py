import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('alien_invasion/alien_invasion_sprites/spaceship.png')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom middle of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag; start with a ship that's not moving.
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

        self.visible = True

        # Opacity for blinking effect.
        self.blinking = False
        self.timer = 30
        self.toggle_timer = 0
        self.alpha = 255


    def update(self, dt):
        """Update the ship's position based on the movement flags."""
        # Update the ship's x or y value, not the rect.
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

        # Update rect object from self.y.
        self.rect.y = self.y


    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = self.screen_rect.bottom - self.rect.height


    def blink_after_hit(self):
        """Make the ship blink to indicate it was hit."""
        if self.blinking:
            self.toggle_timer += 1
            if self.toggle_timer % 10 == 0:  # Toggle visibility every 10 frames
                self.alpha = 0 if self.alpha == 255 else 255
                self.image.set_alpha(self.alpha)

            # Decrease blink duration
            self.blink_timer -= 1
            if self.blink_timer <= 0:
                # Reset blinking state
                self.blinking = False
                self.alpha = 255
                self.image.set_alpha(self.alpha)


    def blitme(self):
        """Draw the ship at its current location."""
        if self.visible:
            self.screen.blit(self.image, self.rect)
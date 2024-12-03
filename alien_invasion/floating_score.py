import pygame
from scoreboard import Scoreboard

class FloatingScore(pygame.sprite.Sprite):
    """A class to display floating score values when aliens are hit."""

    def __init__(self, ai_game, x, y, score_value):
        """Initialize the floating score."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.font = pygame.font.Font("alien_invasion/alien_invasion_sprites/upheavtt.ttf", 24)

        self.start_color = (255, 255, 255)  # Start with white
        self.end_color = (255, 241, 87) # Transition to yellow
        self.current_color = self.start_color

        self.score_value = score_value

        self.image = Scoreboard.render_text_with_outline(self, str(self.score_value), self.font, self.current_color, (0, 0, 0), 2)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.y = float(self.rect.y)  # Store a float for smooth upward movement
        self.timer = 60  # Total lifespan of the floating score


    def _interpolate_color(self):
        """Calculate the current color based on the timer."""
        progress = 1 - (self.timer / 60)  # Calculate how far along we are (0 to 1)
        r = int(self.start_color[0] + (self.end_color[0] - self.start_color[0]) * progress)
        g = int(self.start_color[1] + (self.end_color[1] - self.start_color[1]) * progress)
        b = int(self.start_color[2] + (self.end_color[2] - self.start_color[2]) * progress)
        return (r, g, b)


    def update(self):
        """Move the score up, change its color, and count down its timer."""
        # Move the score upward
        if self.timer >= 40:
            self.y -= 1
            self.rect.y = self.y

        # Update the current color
        self.current_color = self._interpolate_color()

        # Update the image with the new color
        self.image = Scoreboard.render_text_with_outline(self, str(self.score_value), self.font, self.current_color, (0, 0, 0), 2)

        # Decrease the lifespan timer and remove the score when it expires
        self.timer -= 1
        if self.timer <= 0:
            self.kill()


    def draw(self):
        """Draw the floating score to the screen."""
        self.screen.blit(self.image, self.rect)
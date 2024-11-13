# Difficulty: 2/10 Very easy, just had to follow the book.
# This code create a program window of a blue screen that's color can be adjusted in the settings class.

import sys
import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (0, 0, 255)

    def run_game(self):
        """Initialize the game, and create game resources."""
        while True:
            """Start the main loop for the game."""
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.settings.bg_color)
            
            pygame.display.flip()
            self.clock.tick(60)


class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 255)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
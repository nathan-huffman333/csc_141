# Difficulty: 6/10 A bit challenging, however I wanted to add some things to it to make it more unique and appear nicer.
# This code has raindrops appear in a random arrangment at the top of the screen and fall down at different speeds.

import sys
import pygame
from settings import Settings
from raindrop import Raindrop
from random import randint
from cloud import Cloud

class RainInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Rain Invasion")

        self.cloud = Cloud(self)
        self.raindrops = pygame.sprite.Group()
        self.last_raindrop_time = 0


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_raindrops()
            self._create_raining()
            self._update_screen()
            self.clock.tick(60)
                    
    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)


    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_ESCAPE:
            sys.exit()
 

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)
        self.cloud.blitme()
        pygame.display.flip()


    def _create_raining(self):
        """Create many raindrops to make it appear like it is raining."""
        current_time = pygame.time.get_ticks()
        if current_time - self.last_raindrop_time > 25: 
            self.last_raindrop_time = current_time
            x_position = randint(60, self.settings.screen_width - 60)
            y_position = randint(60, 80)
            self._create_raindrop(x_position, y_position)


    def _create_raindrop(self, x_position, y_position):
        """Create a raindrop and place it in row to appear like it is raining."""
        new_raindrop = Raindrop(self)
        new_raindrop.y = y_position
        new_raindrop.rect.x = x_position
        new_raindrop.rect.y = y_position
        self.raindrops.add(new_raindrop)


    def _update_raindrops(self):
        """Check if the raindrops are at an edge, then update positions."""
        self.raindrops.update()
        for raindrop in self.raindrops.copy():
            if raindrop.rect.top >= self.settings.screen_height:
                self.raindrops.remove(raindrop)


    def _check_raindrop_edges(self):
        """Respond appropriately if any raindrops have reached an edge."""
        for raindrop in self.raindrops.sprites():
            if raindrop.check_raindrop_edges():
                self.raindrops.remove(raindrop)



if __name__ == '__main__':
    # Make a game instance, and run the game.
    ri = RainInvasion()
    ri.run_game()
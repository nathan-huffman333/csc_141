# Difficulty: 2/10 I just rewrote some of the alien code to move only downwards and make it be raindrops instead of aliens, not too bad.
# This code makes a grid of raindrops fall from the top of the screen. 

import sys
import pygame
from settings import Settings
from raindrop import Raindrop
from star import Star
from random import randint

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
        
        self.stars = pygame.sprite.Group()
        self._create_stars()

        self.bullets = pygame.sprite.Group()
        self.raindrops = pygame.sprite.Group()

        self._create_raining()


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_raindrops()
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
        
        self.stars.draw(self.screen)

        self.raindrops.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


    def _create_raining(self):
        """Create many raindrops to make it appear like it is raining."""
        # Create an raindrop and keep adding raindrops until there's no room left.
        # Spacing between raindrops is one raindrop width and one raindrop height.
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size

        current_x, current_y = raindrop_width, raindrop_height
        while current_y < (self.settings.screen_height - 5 * raindrop_height):
            while current_x < (self.settings.screen_width - 2 * raindrop_width):
                self._create_raindrop(current_x, current_y)
                current_x += 2 * raindrop_width
        
            # Finshed a row; reset x value, and increment y value.
            current_x = raindrop_width
            current_y += 2 * raindrop_height


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


    def _check_raindrop_edges(self):
        """Respond appropriately if any raindrops have reached an edge."""
        for raindrop in self.raindrops.sprites():
            if raindrop.check_raindrop_edges():
                self.raindrops.remove(raindrop)
                break


    def _create_stars(self):
        """Create the starscape."""
        for stars in range(250):
            x_position = randint(10, self.settings.screen_width - 10)
            y_position = randint(10, self.settings.screen_height - 10)
            self._create_star(x_position, y_position)
         

    def _create_star(self, x_position, y_position):
        new_star = Star(self)
        new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star) 



if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = RainInvasion()
    ai.run_game()
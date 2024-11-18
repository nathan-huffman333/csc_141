# Difficulty 4/10 A little difficult to try and create the program on my own, but after looking back at previous code it wasn't too bad.
# This code creates a program that prints the exact key that is pressed by the user.

import sys
import pygame

class Keys:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Keys")

    
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)


    def _check_keydown_events(self, event):
        print(pygame.key.name(event.key))
        if event.key == pygame.K_ESCAPE:
            sys.exit()


    def _update_screen(self):
        self.screen.fill(color=(255,255,255))
        pygame.display.flip()


if __name__ == '__main__':
    ai = Keys()
    ai.run_game()
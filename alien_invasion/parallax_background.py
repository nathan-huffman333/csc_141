import pygame

class ParallaxBackground:
    """Manages a parallax scrolling background."""
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        # Load background layers
        self.layers = [
            pygame.image.load("alien_invasion/alien_invasion_sprites/backgrounds/background_1.png").convert_alpha(),
            pygame.image.load("alien_invasion/alien_invasion_sprites/backgrounds/background_2.png").convert_alpha()
        ]

        # Scale layers to fit the screen
        self.layers = [pygame.transform.scale(layer, (settings.screen_width, settings.screen_height)) for layer in self.layers]

        # Initial positions for scrolling
        self.layer_positions = [0, 0, 0]

        # Scrolling speeds for each layer
        self.scroll_speeds = [3.0, 4.5] # Adjust speeds as needed


    def update(self, dt):
        """Update the vertical position of each background layer."""
        for i, speed in enumerate(self.scroll_speeds):
            self.layer_positions[i] += speed * dt * 100  # Speed adjusted for frame time

            # Wrap layer position to create seamless scrolling
            if self.layer_positions[i] >= self.settings.screen_height:
                self.layer_positions[i] = 0


    def draw(self):
        """Draw the layers on the screen."""
        for i, layer in enumerate(self.layers):
            # Blit the layer twice for seamless scrolling
            self.screen.blit(layer, (0, self.layer_positions[i]))
            self.screen.blit(layer, (0, self.layer_positions[i] - self.settings.screen_height))

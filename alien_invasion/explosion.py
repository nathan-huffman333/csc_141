import pygame
from pygame.sprite import Sprite

class Explosion(Sprite):
    """A class to manage explosions."""

    def __init__(self, ai_game, center):
        """Initialize the explosion."""
        super().__init__()
        self.screen = ai_game.screen
        self.frames = self._load_frames()
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.animation_speed = 5  # Number of frames before switching

        # Timer to control animation speed
        self.frame_counter = 0


    def _load_frames(self):
        """Load the frames for the explosion animation."""
        frames = []
        for i in range(1, 12):  # Assume you have 11 frames named explosion1.png to explosion11.png
            frame = pygame.image.load(f"alien_invasion/alien_invasion_sprites/explosion/explosion_{i}.png")
            frames.append(frame)
        return frames


    def update(self):
        """Update the explosion animation."""
        self.frame_counter += 1
        if self.frame_counter >= self.animation_speed:
            self.frame_counter = 0
            self.current_frame += 1
            if self.current_frame < len(self.frames):
                self.image = self.frames[self.current_frame]
            else:
                self.kill()  # Remove the explosion sprite when done

    
    def draw(self):
        """Draw the explosion to the screen."""
        self.screen.blit(self.image, self.rect)
import pygame

__all__ = ['Background']

# Global image cache to avoid repeated loading
_image_cache = {}

def load_cached_image(path):
    """Load and cache images to avoid repeated disk access"""
    if path not in _image_cache:
        _image_cache[path] = pygame.image.load(path)
    return _image_cache[path]


class Background(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.length = 800
        self.image = load_cached_image("images/background.png")  # Use cached loading

    def update(self, screen, plane_vel):
        self.x -= plane_vel.x
        self.y -= plane_vel.y
        if self.x < -self.length:
            self.x = self.length
        elif self.x > self.length:
            self.x = -self.length
        if self.y < -self.length:
            self.y = self.length
        elif self.y > self.length:
            self.y = -self.length
        screen.blit(self.image, (self.x, self.y))

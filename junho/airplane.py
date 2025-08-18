import pygame
from yejun.methods import *

__all__ = ['Airplane', 'Jetplane', 'Spaceship']

# Global image cache to avoid repeated loading
_image_cache = {}

def load_cached_image(path):
    """Load and cache images to avoid repeated disk access"""
    if path not in _image_cache:
        _image_cache[path] = pygame.image.load(path)
    return _image_cache[path]


class Airplane(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = None
        self.display_image = None
        self.rect = None
        self.mask = None
        self.width = None
        self.height = None
        self.trans_speed = None
        self.rot_speed = None
        self.loc = None
        self.vel = None
        self.cnt = None
        
        # Performance optimization: Cache rotated images
        self.rotation_cache = {}
        self.last_angle = None
        self.angle_threshold = 3  # More precise for player control
        
        self.set_speeds(6, 3)
        self.set_initial(x, y, angle)
        self.set_image('images/airplane1.png')

    def set_speeds(self, trans_speed, rot_speed):  # 병진, 회전 속력 설정
        self.trans_speed = trans_speed
        self.rot_speed = rot_speed

    def set_initial(self, x, y, angle):  # 초기 위치 및 방향 설정
        self.loc = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2()
        self.vel.from_polar((self.trans_speed, angle))
        self.cnt = 0

    def set_image(self, path):  # 이미지 고르고 위치 설정
        self.image = load_cached_image(path)  # Use cached loading
        self.display_image = self.image
        self.rect = self.display_image.get_rect().move(self.loc.x, self.loc.y)
        self.mask = pygame.mask.from_surface(self.display_image)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def get_rotated_image(self, angle):
        """Get cached rotated image or create and cache new one"""
        # Round angle to nearest threshold to reduce cache size
        rounded_angle = round(angle / self.angle_threshold) * self.angle_threshold
        
        if rounded_angle not in self.rotation_cache:
            rotated = pygame.transform.rotate(self.image, -90 - rounded_angle)
            self.rotation_cache[rounded_angle] = rotated
            
            # Limit cache size to prevent memory bloat
            if len(self.rotation_cache) > 120:  # 360/3 = 120 possible angles
                # Remove oldest entries
                keys_to_remove = list(self.rotation_cache.keys())[:20]
                for key in keys_to_remove:
                    del self.rotation_cache[key]
        
        return self.rotation_cache[rounded_angle]

    def update(self, screen, pic=None):
        pressed = pygame.key.get_pressed()
        right = pressed[pygame.K_RIGHT]
        left = pressed[pygame.K_LEFT]
        if right and left:
            delta_theta = 0
        elif right:
            delta_theta = self.rot_speed
        elif left:
            delta_theta = -self.rot_speed
        else:
            delta_theta = 0

        self.vel = self.vel.rotate(delta_theta)
        _, theta = self.vel.as_polar()
        
        # Only update display image if angle changed significantly
        if self.last_angle is None or abs(theta - self.last_angle) > self.angle_threshold:
            self.display_image = self.get_rotated_image(theta)
            self.last_angle = theta
            # Only recalculate mask when image changes
            self.mask = pygame.mask.from_surface(self.display_image)
        
        self.rect = center_rect(self)
        center_blit(screen, self)


class Jetplane(Airplane):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.set_speeds(7, 2)
        self.set_initial(x, y, angle)
        self.set_image("images/airplane2.png")


class Spaceship(Airplane):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.set_speeds(5, 4)
        self.set_initial(x, y, angle)
        self.set_image("images/airplane3.png")

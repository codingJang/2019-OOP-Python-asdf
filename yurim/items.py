import pygame
import random
from yejun.methods import *

__all__ = ['Item', 'make_items']

# Global image cache to avoid repeated loading
_image_cache = {}

def load_cached_image(path):
    """Load and cache images to avoid repeated disk access"""
    if path not in _image_cache:
        _image_cache[path] = pygame.image.load(path)
    return _image_cache[path]


class Item(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.loc = None  # pygame.math.Vector2
        self.image = None
        self.display_image = None
        self.rect = None
        self.mask = None
        self.width = None
        self.height = None
        self.time = 0
        self.kill_time = None
        
        # Performance optimization: Items don't rotate, so we can cache mask
        self.mask_cached = False
        
        self.set_location(x, y)
        self.set_image('images/star.png')  # 이미지 고르고 위치 설정
        self.set_kill_time(1800)  # kill time 설정

    def set_location(self, x, y):  # 초기 위치 및 방향 설정
        self.loc = pygame.math.Vector2(x, y)

    def set_image(self, path):  # 이미지 고르고 위치 설정
        self.image = load_cached_image(path)  # Use cached loading
        self.display_image = self.image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = center_rect(self)
        self.mask = pygame.mask.from_surface(self.display_image)
        self.mask_cached = True

    def set_kill_time(self, kill_time):
        self.kill_time = kill_time

    def update(self, screen, plane_vel):
        self.loc -= plane_vel
        self.rect = center_rect(self)
        # Don't recalculate mask since item image doesn't change
        # self.mask = pygame.mask.from_surface(self.display_image)  # Removed for performance
        center_blit(screen, self)
        self.time += 1
        if self.time >= self.kill_time:
            self.kill()


def make_items(sprites, time):
    ran_num = random.randint(1, 100)
    # Reduced frequency slightly for better performance
    if time % 5 == 0 and ran_num > 96:  # Was 95, now 96 for fewer items
        ran_x = random.randint(1, 799)
        ran_y = random.randint(1, 799)
        sprites.add(Item(ran_x, ran_y))

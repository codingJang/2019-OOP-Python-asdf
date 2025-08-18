# coding=utf-8
"""
Performance-optimized version of the missile dodging game
Key optimizations:
- Cached font objects
- Reduced redundant operations
- Optimized collision detection
- Better memory management
"""

import pygame  # pygame 가져오기
from yejun.missile import *  # 장예준이 만든 Missile 클래스
from junho.airplane import *  # 장준호가 만든 Airplane 클래스
from yurim.background import *  # 이유림이 만든 Background 클래스
from yurim.button import *
from yurim.items import *

pygame.init()

# Performance optimizations: Cache commonly used objects
class GameResources:
    """Cache for expensive-to-create objects"""
    def __init__(self):
        # Pre-load and cache font objects (very expensive to create each frame)
        self.fonts = {
            'small': pygame.font.Font("Teko-Regular.ttf", 40),
            'medium': pygame.font.Font("Teko-Regular.ttf", 50),
        }
        
        # Cache for rendered text surfaces to avoid re-rendering identical text
        self.text_cache = {}
        
        # FPS tracking for performance monitoring
        self.fps_samples = []
        self.show_fps = False  # Toggle with F key
    
    def get_text_surface(self, text, font_size='small', color=(0, 0, 0)):
        """Get cached text surface or create and cache new one"""
        cache_key = (text, font_size, color)
        if cache_key not in self.text_cache:
            font = self.fonts[font_size]
            self.text_cache[cache_key] = font.render(text, True, color)
        return self.text_cache[cache_key]
    
    def clear_text_cache(self):
        """Clear text cache to prevent memory bloat"""
        if len(self.text_cache) > 100:  # Limit cache size
            self.text_cache.clear()

# Initialize game resources
resources = GameResources()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Missiles! - Optimized")

backgrounds = pygame.sprite.Group()
bg_length = 800
backgrounds.add(Background(0, 0), Background(bg_length, 0),
                Background(0, bg_length), Background(bg_length, bg_length))

options = pygame.sprite.Group()
items = pygame.sprite.Group()

# 시작 화면
chooseButton = Button((0, 223, 0), 220, 550, 360, 80, 'Choose your airplane!')
options.add(chooseButton)
make_button(screen, options, "images/startBackground.png")
options.remove(chooseButton)

# 비행기 옵션 선택
user_plane = None
option1 = Button((0, 255, 0), 80, 500, 200, 80, 'Option 1', 1)
option2 = Button((0, 255, 0), 300, 500, 200, 80, 'Option 2', 2)
option3 = Button((0, 255, 0), 520, 500, 200, 80, 'Option 3', 3)
startButton = Button((0, 255, 0), 80, 600, 200, 80, 'Game start', 1)
backButton = Button((0, 255, 0), 520, 600, 200, 80, 'Back', 2)

page = True
while page:
    options.add(option1, option2, option3)
    op = make_button(screen, options, "images/airplanebackground.png")
    if op:
        options.remove(option1, option2, option3)
        options.add(startButton, backButton)
        re = 2
        if op == 1:
            re = make_button(screen, options, "images/airplanetext.png")
            user_plane = Airplane(400, 400, -90)
        elif op == 2:
            re = make_button(screen, options, "images/Jetplanetext.png")
            user_plane = Jetplane(400, 400, -90)
        elif op == 3:
            re = make_button(screen, options, "images/stealthtext.png")
            user_plane = Spaceship(400, 400, -90)
        options.remove(startButton, backButton)
        if re == 1:
            page = False
        else:
            continue

missiles = pygame.sprite.Group()  # 미사일들을 관리하는 Group 객체 missiles 생성

clock = pygame.time.Clock()  # clock (화면 리프레시 속도 조절용)
start_time = pygame.time.get_ticks()    # 게임 시작 시간 저장

running = True
bonus = 5
level = 1
frame_count = 0

# Performance tracking variables
last_fps_update = 0
current_fps = 60

while running:
    frame_count += 1
    current_time = pygame.time.get_ticks()
    
    # Update FPS display every second
    if current_time - last_fps_update > 1000:
        current_fps = clock.get_fps()
        resources.fps_samples.append(current_fps)
        if len(resources.fps_samples) > 60:  # Keep last 60 samples
            resources.fps_samples.pop(0)
        last_fps_update = current_time
    
    events = pygame.event.get()  # 이벤트 모음
    for event in events:
        if event.type == pygame.QUIT:  # 닫으면 나가기
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:  # Toggle FPS display with F key
                resources.show_fps = not resources.show_fps
    
    screen.fill((102, 204, 255))    # 배경 사이 틈 같은색으로 매꾸기

    time_since_enter = (current_time - start_time) // 1000 + bonus  # 게임 시작 이후 진행 시간을 점수로 표시(초 단위)

    # Only recalculate level when it actually changes
    new_level = time_since_enter // 10 + 1
    delta_level = new_level - level
    level = new_level

    add_missile(missiles, level, user_plane.loc)  # 게임 레벨에 따른 미사일 생성
    make_items(items, time_since_enter)  # 아이템 생성

    backgrounds.update(screen, user_plane.vel)  # backgrounds Group 내의 모든 background 에 대해 update() 함수 실행
    user_plane.update(screen)  # user_plane 의 업데이트 실행
    items.update(screen, user_plane.vel)  # items 에 대해 실행
    missiles.update(screen, user_plane.loc, user_plane.vel)  # missiles 에 대해 실행

    # Optimized text rendering using cached surfaces
    level_text = resources.get_text_surface('Level ' + str(level))
    screen.blit(level_text, (10, 5))
    
    score_text = resources.get_text_surface('Score : ' + str(time_since_enter))
    screen.blit(score_text, (10, 40))
    
    bonus_text = resources.get_text_surface('bonus : ' + str(bonus))
    screen.blit(bonus_text, (680, 5))
    
    # Optional FPS display for performance monitoring
    if resources.show_fps:
        fps_text = resources.get_text_surface(f'FPS: {current_fps:.1f}')
        screen.blit(fps_text, (10, 75))
        
        # Show missile and item counts for debugging
        debug_text = resources.get_text_surface(f'Missiles: {len(missiles)} Items: {len(items)}')
        screen.blit(debug_text, (10, 110))

    # Optimized collision detection - only check if objects exist
    if items:
        # 비행기 - 아이템 충돌 검출
        plane_items_collisions = pygame.sprite.spritecollide(user_plane, items, True,
                                                             collided=pygame.sprite.collide_mask)
        bonus += len(plane_items_collisions)

    if missiles:
        # 비행기 - 미사일 충돌 검출
        plane_missiles_collisions = pygame.sprite.spritecollide(user_plane, missiles, True,
                                                                collided=pygame.sprite.collide_mask)
        if len(plane_missiles_collisions) != 0:  # 비행기와 미사일이 충돌했다면
            question1 = resources.get_text_surface('Do you want to replay?', 'medium')
            question2 = resources.get_text_surface('If you have more than five bonus, you can continue!', 'medium')
            # 게임 진행 여부 버튼
            replayButton = Button((0, 255, 0), 80, 450, 200, 80, 'Replay', 1)
            endButton = Button((0, 255, 0), 300, 450, 200, 80, 'End', 2)
            options.add(replayButton, endButton)
            continueButton = Button((0, 255, 0), 520, 450, 200, 80, 'continue', 3)
            if bonus >= 5:
                options.add(continueButton)
            else:
                pygame.draw.rect(screen, (200, 200, 200), (520, 450, 200, 80), 0)
                text = resources.get_text_surface("continue", 'medium')
                screen.blit(text, (520 + (100 - text.get_width() / 2), 450 + (40 - text.get_height() / 2)))
            screen.blit(question1, (240, 280))
            screen.blit(question2, (30, 350))
            re = make_button(screen, options)
            if continueButton in options:
                options.remove(continueButton)
            if re == 1:
                missiles.empty()
                items.empty()
                user_plane.set_initial(400, 400, -90)
                start_time = pygame.time.get_ticks()  # 게임 시작 시간 저장
                bonus = 0
                resources.clear_text_cache()  # Clear cache on restart
            if re == 2:
                running = False
            if re == 3:
                bonus -= 5
                pass

        # 미사일 간 충돌 검출 - 최적화된 버전
        if len(missiles) > 1:  # Only check if more than 1 missile
            missiles_collisions = pygame.sprite.groupcollide(missiles, missiles, False, False,
                                                             collided=pygame.sprite.collide_mask)
            missiles_to_remove = set()
            for missile1 in missiles_collisions:
                for missile2 in missiles_collisions[missile1]:
                    if missile1 is not missile2 and missile1 not in missiles_to_remove and missile2 not in missiles_to_remove:
                        missiles_to_remove.add(missile1)
                        missiles_to_remove.add(missile2)
                        bonus += 1
            
            # Remove collided missiles
            for missile in missiles_to_remove:
                missile.kill()

    # Clear text cache periodically to prevent memory bloat
    if frame_count % 1000 == 0:
        resources.clear_text_cache()

    pygame.display.update()
    clock.tick(60)  # 화면 리프레시 속도 조절 (60 frames per second)

import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        raw_image = pygame.image.load("assets/sprites/Player.png").convert_alpha()
        self.original_image = pygame.transform.scale(raw_image, (64,64))
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5
        
        self.score = 0
        self.lives = 3
        
        self.facing_dx = 0
        self.facing_dy = 1
        
        self.last_shot_time = -100
        self.shoot_cd = 100
        
        self.last_explode_time = -500
        self.explode_cd = 5000
        
    def update(self, keys, Width, Height):
        
        dx = 0
        dy = 0 
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy = -1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy = 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = 1

        if dx != 0 and dy != 0:
            length = math.sqrt(dx ** 2 + dy ** 2)
            dx /= length
            dy /= length

            self.rect.x += int(dx * self.speed)
            self.rect.y += int(dy * self.speed)
        
        if (int(dx != 0) ^ int(dy != 0)):
            
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed
            
        if dx != 0 or dy != 0:
            self.facing_dx = dx
            self.facing_dy = dy
            angle = math.degrees(math.atan2(dx, dy))
            old_center = self.rect.center
            self.image = pygame.transform.rotate(self.original_image, angle)
            self.rect = self.image.get_rect()
            self.rect.center = old_center
            
        if self.rect.y < 0:
                self.rect.y = Height
        if self.rect.y > Height:
                self.rect.y = 0
        if self.rect.x < 0:
                self.rect.x = Width
        if self.rect.x > Width:
                self.rect.x = 0
                

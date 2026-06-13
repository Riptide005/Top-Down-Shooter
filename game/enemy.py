import pygame 
import math

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.original_image = pygame.image.load("assets/sprites/Enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (32,32))
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.exact_x = float(x)
        self.exact_y = float(y)
        
        self.speed = 2
        self.radius = int((self.rect.width // 2) * 0.8)
        self.hitbox = self.rect.inflate(-5, -5)
        
    def update(self, player):
        
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        
        distance = math.sqrt(dx ** 2 + dy ** 2)
        
        if distance > 0:
            
            dx /= distance
            dy /= distance
            
            self.exact_x += dx * self.speed
            self.exact_y += dy * self.speed

            self.rect.centerx = int(self.exact_x)
            self.rect.centery = int(self.exact_y)
            
            self.hitbox.center = self.rect.center
            
            angle = math.degrees(math.atan2(dx, dy))
            self.image = pygame.transform.rotate(self.original_image, angle)
            self.rect = self.image.get_rect()
            self.rect.center = self.hitbox.center
            
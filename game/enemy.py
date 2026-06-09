import pygame 
import math

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.original_image = pygame.image.load("assets/sprites/Enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (32,32))
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.speed = 2
        
    def update(self, player):
        
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        
        distance = math.sqrt(dx ** 2 + dy ** 2)
        
        if distance > 0:
            dx /= distance
            dy /= distance
            
            self.rect.x += int(dx * self.speed)
            self.rect.y += int(dy * self.speed)

            angle = math.degrees(math.atan2(dx, dy))
            old_center = self.rect.center
            self.image = pygame.transform.rotate(self.original_image, angle)
            self.rect = self.image.get_rect()
            self.rect.center = old_center
            
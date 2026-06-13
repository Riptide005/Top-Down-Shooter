import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy):
        
        super() .__init__()
        self.raw_image = pygame.image.load("assets/sprites/shot.png").convert_alpha()
        self.original_image = pygame.transform.scale(self.raw_image, (9,32))
        
        if dx != 0 or dy != 0: 
            angle = math.degrees(math.atan2(dx, dy))
            self.image = pygame.transform.rotate(self.original_image, angle)
        else:
            self.image = self.original_image
        
        self.rect = self.image.get_rect(center = (x, y))
        self.hitbox = self.rect.inflate(-4, -4)
        
        self.pos_x = float(x)
        self.pos_y = float(y)
        self.dx = dx
        self.dy = dy
        self.speed = 10
        
    def update(self, *args):
        
        if self.dx != 0 or self.dy != 0:
            length = math.sqrt(self.dx ** 2 + self.dy ** 2)
            self.dx /= length
            self.dy /= length

            self.pos_x += self.dx * self.speed
            self.pos_y += self.dy * self.speed
            self.rect.centerx = int(self.pos_x)
            self.rect.centery = int(self.pos_y)
            
            self.hitbox.center = self.rect.center

        if not (-50 < self.hitbox.centerx < 850 and -50 < self.hitbox.centery < 650):
            self.kill()
        
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.raw_image = pygame.image.load("assets/sprites/Explosion.png")
        self.radius = 20
        self.max_radius = 200
        self.growth_rate = 10
        
        start_diameter = 2 * self.radius
        self.image = pygame.transform.scale(self.raw_image, (start_diameter, start_diameter))
        self.rect = self.image.get_rect(center = (x, y))
        
    def update(self, *args):
        
        self.radius += self.growth_rate
        
        if self.radius >= self.max_radius:
            self.kill()
        
        else:
            new_diameter = int(self.radius * 2)
            self.image = pygame.transform.scale(self.raw_image, (new_diameter, new_diameter))
            
            old_center = self.rect.center
            self.rect = self.image.get_rect(center = old_center)
            
        
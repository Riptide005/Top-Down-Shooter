import sys
import pygame
import numpy as np
from player import Player
from enemy import Enemy
from weapons import Bullet,Explosion


pygame.init()
pygame.font.init()
font_small = pygame.font.Font(None, size = 14)
font_large = pygame.font.Font(None, size = 32)

running = True
clock = pygame.time.Clock()

Width = 800
Height = 600
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Top Down Shooter Game")

player = Player(Width // 2, Height // 2)

enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
explosions = pygame.sprite.Group()

#Spawner for enemies

def enemy_spawner(): 
    
    if np.random.randint(0,51) == 50:
        x = 2 * np.random.randint(0,2) - 1
        y = 2 * np.random.randint(0,2) - 1
        new_enemy = Enemy(900 * x, 700 * y)
        enemies.add(new_enemy)
    

#Shooting and Explosion function

def abilities(keys, player, bullet, explosion):
    current_time = pygame.time.get_ticks()
    if keys[pygame.K_SPACE] and current_time - player.last_shot_time > player.shoot_cd:
        player.last_shot_time = current_time
        spawnx = player.rect.centerx
        spawny = player.rect.centery
        aimx = player.facing_dx
        aimy = player.facing_dy
        new_bullet = Bullet(spawnx, spawny, aimx, aimy)
        bullets.add(new_bullet)

    if keys[pygame.K_e] and current_time - player.last_explode_time > player.explode_cd:
        player.last_explode_time = current_time
        epicenterx = player.rect.centerx 
        epicentery = player.rect.centery
        new_explosion = Explosion(epicenterx, epicentery)
        explosions.add(new_explosion)

def death(player, enemy, bullets, explosions):
    killed_enemies = pygame.sprite.groupcollide(enemies, bullets, True, True)
    player.score += len(killed_enemies)
    
    for exp in explosions:
        for e in enemies:
            dist = np.sqrt(((exp.radius) - e.rect.centerx) ** 2 + ((exp.radius) - e.rect.centery) ** 2)
            if dist <= exp.radius:
                e.kill()
                player.score += 1
                
    player_hit = pygame.sprite.spritecollide(player, enemies, True)
    
    if len(player_hit) != 0:
        player.lives -= 1
        
    if player.lives == 0:
        global running;
        running = False

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    
    player.update(keys, Width, Height)
    
    enemy_spawner()
    abilities(keys, player, Bullet, Explosion)
    
    for e in enemies:
        e.update(player)
    
    bullets.update()
    explosions.update()
    
    
    screen.fill((30,30,30))
    
    death(player, enemies, bullets, explosions)
    

    explosions.draw(screen)
    enemies.draw(screen)
    
    bullets.draw(screen)
    current_lives = font_large.render(f"Lives = {player.lives}", True, (255, 0, 0))
    current_score = font_large.render(f"Score = {player.score}", True, (255, 0, 255))
    screen.blit(player.image , player.rect)
    screen.blit(current_score, (10, 10))
    screen.blit(current_lives, (700, 10))
    
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
sys.exit()
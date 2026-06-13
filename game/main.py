import sys
import pygame
import numpy as np
from player import Player
from enemy import Enemy
from weapons import Bullet,Explosion


pygame.init()
pygame.font.init()
font_small = pygame.font.Font(None, size = 20)
font_medium = pygame.font.Font(None, size = 26)
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

game_mode = "START_MENU"


#Spawner for enemies
def start_screen(screen):
    screen.fill((30, 30, 30))
    menu_text = font_large.render("Welcome to Top Down Arena", True, (255, 255, 255))
    menu_start = font_medium.render("Press Space to Start!", True, (255, 255, 255))
    
    screen.blit(menu_text, (260, 220))
    screen.blit(menu_start, (322, 280))
    
    pygame.display.flip()
    for event in current_events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            return "PLAYING"
    return "START_MENU"


def game_running(screen, player, enemies, bullets, explosion):
    
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

    mini_player_icon = pygame.transform.scale(player.original_image, (24, 24))
    start_x = 770 
    for i in range(player.lives):

        icon_x = start_x - (i * 30) 
        screen.blit(mini_player_icon, (icon_x, 10))
        
    current_score = font_small.render(f"Score = {player.score}", True, (255, 0, 255))
    screen.blit(player.image , player.rect)
    screen.blit(current_score, (10, 10))
    
    pygame.display.flip()
    
    clock.tick(60)
    if player.lives <= 0:
        return "GAME_OVER"  
    return "PLAYING"

def reset_game(player, enemies, bullets, explosions, screen):
    enemies.empty()
    bullets.empty()
    explosions.empty()
    
    player.lives = 3
    player.score = 0
    
    player.rect.center = (Width // 2, Height // 2)

def show_game_over(screen, player, enemies, bullets, explosions, events):
    screen.fill((50, 10, 10)) 
    
    over_text = font_large.render("GAME OVER", True, (255, 50, 50))
    score_text = font_medium.render(f"Final Score: {player.score}", True, (255, 255, 255))
    retry_text = font_small.render("Press 'R' to Retry or 'ESC' to Quit", True, (200, 200, 200))
    
    center_x = screen.get_width() // 2
    screen.blit(over_text, over_text.get_rect(center=(center_x, 200)))
    screen.blit(score_text, score_text.get_rect(center=(center_x, 260)))
    screen.blit(retry_text, retry_text.get_rect(center=(center_x, 320)))
    
    pygame.display.flip()
    
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game(player, enemies, bullets, explosions, screen)
                return "PLAYING"
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                
    return "GAME_OVER"
    
def enemy_spawner(): 
    
    if np.random.randint(0,51) == 50:
        x = 2 * np.random.randint(0,2) - 1
        y = 2 * np.random.randint(0,2) - 1
        new_enemy = Enemy(900 * x, 700 * y)
        enemies.add(new_enemy)
    

#Shooting and Explosion function

def custom_bullet_hitbox_check(enemy, bullet):
    return enemy.hitbox.colliderect(bullet.hitbox)

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
    
    killed_enemies = pygame.sprite.groupcollide(enemies, bullets, True, True, collided = custom_bullet_hitbox_check)
    player.score += len(killed_enemies)
    
    for exp in explosions:
        hits = pygame.sprite.spritecollide(exp, enemies, True, pygame.sprite.collide_circle)
        player.score += len(hits)
        
    for e in enemies: 
        if player.hitbox.colliderect(e.hitbox):
            player.lives -= 1
            e.kill()
        

while running:
    
    current_events = pygame.event.get()
    for event in current_events:
        if event.type == pygame.QUIT:
            running = False
    
    if game_mode == "START_MENU":
        game_mode = start_screen(screen)
    elif game_mode == "PLAYING":
        game_mode = game_running(screen, player, enemies, bullets, explosions)
    elif game_mode == "GAME_OVER":
        game_mode = show_game_over(screen, player, enemies, bullets, explosions, current_events)

pygame.quit()
sys.exit()
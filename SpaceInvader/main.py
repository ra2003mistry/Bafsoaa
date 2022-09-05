import pygame
import random

pygame.init()

# creating screen
screen = pygame.display.set_mode((800, 800))

# Title and icon
pygame.display.set_caption('Space Invader')
icon = pygame.image.load('rocket(1).png')
pygame.display.set_icon(icon)
running = True
# Player
player_icon = pygame.image.load('spaceship(1).png')
playerX = 360
playerY = 630
playerX_co = 0
playerY_co = 0
# enemy
enemy_icon = pygame.image.load('enemy(1).png')
enemyX = random.randit(0, 800)
enemyY = random.randit(50, 150)
enemyX_co = 0.3

def player(x, y):
    screen.blit(player_icon, (x, y))
  
def enemy(x, y):
    screen.blit(enemy_icon, (x, y))
# Game loop

while running:

    screen.fill((0, 0, 0))

    for task in pygame.event.get():
        if task.type == pygame.QUIT:
            running = False
        # checking keys
        if task.type == pygame.KEYDOWN:
            if task.key == pygame.K_LEFT:
                playerX_co = -0.3
            if task.key == pygame.K_RIGHT:
                playerX_co = 0.3
            if task.key == pygame.K_UP:
                playerY_co = -0.3
            if task.key == pygame.K_DOWN:
                playerY_co = 0.3

        if task.type == pygame.KEYUP:
            if task.key == pygame.K_LEFT or task.key == pygame.K_RIGHT:
                playerX_co = 0
            if task.key == pygame.K_UP or task.key == pygame.K_DOWN:
                playerY_co = 0

    playerX += playerX_co
    playerY += playerY_co
    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    # enemy movements    
    enemyX += enemyX_co
    if enemyX <= 0:
        enemyX_co = 0.5
    elif enemyX >= 736:
        enemyX_co = -0.5
    
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    
    pygame.display.update()

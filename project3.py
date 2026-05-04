"""
Mario-like platformer
"""

import pygame

class Game:
    def __init__(self):
        # The game starts as not over
        self.game_over = False

    def player_hit_enemy(self):
         # If the player touches an enemy, the game ends
        self.game_over = True

    def restart(self):
         # Resets the game so the player can try again
        self.game_over = False

# This function checks if the player and enemy are touching
def check_player_enemy_collision(player_rect, enemy_rect):
    return player_rect.colliderect(enemy_rect)

# This function shows a game over message on the screen
def draw_game_over(screen, font):
    text = font.render("Game Over - Press R to Restart", True, (255, 255, 255))
    screen.blit(text, (120, 250))

# Pygame setup
pygame.init()
width = 256 * 3
height = 240 * 3
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 48)

# Load level
level = pygame.image.load('Assets/level.png').convert()
level_surf = pygame.transform.scale(level, (3376 * 3, 480 * 3))

# Game + player setup
game = Game()

player_pos = pygame.Vector2(0, height - 120)
vel_x = 0
vel_y = 0

# Enemy setup
enemy_rect = pygame.Rect(600, height - 120, 48, 48)

running = True
dt = 0

# MAIN LOOP
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Restart game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game.game_over:
                game.restart()
                player_pos = pygame.Vector2(0, height - 120)
                vel_x = 0
                vel_y = 0

    # GAME LOGIC
    if not game.game_over:
        keys = pygame.key.get_pressed()

        # Jump
        if keys[pygame.K_UP]:
            if player_pos.y >= height - 120:
                vel_y = 900 * dt

        # Horizontal movement
        if keys[pygame.K_RIGHT]:
            vel_x = 500 * dt
        elif keys[pygame.K_LEFT]:
            vel_x = -500 * dt
        else:
            vel_x = 0

        # Gravity
        vel_y -= 30 * dt

        # Update position
        player_pos.x += vel_x
        player_pos.y -= vel_y

        # Floor collision
        if player_pos.y >= height - 120:
            player_pos.y = height - 120

        if player_pos.x <= 0:
            player_pos.x = 0

        
        # Collision with enemy
        player_rect = pygame.Rect(
            screen.get_width() // 2 - 24,
            player_pos.y - 24,
            48,
            48
        )

        if check_player_enemy_collision(player_rect, enemy_rect):
            game.player_hit_enemy()

    # DRAWING
    screen.blit(level_surf, (-player_pos.x, 0))

    # Draw player
    pygame.draw.circle(
        screen,
        "firebrick3",
        (screen.get_width() / 2, player_pos.y),
        24
    )

    # Draw enemy
    pygame.draw.rect(
        screen,
        "darkgreen",
        (
            enemy_rect.x - player_pos.x,
            enemy_rect.y,
            enemy_rect.width,
            enemy_rect.height
        )
    )

    # Game over text
    if game.game_over:
        draw_game_over(screen, font)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()

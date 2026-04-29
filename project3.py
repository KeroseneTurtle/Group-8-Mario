"""
Mario-like platformer
"""
# Aniel's part - game state and enemy collision

# This class keeps track of whether the game is still running or game over
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
    # colliderect returns True if the two rectangles overlap
    return player_rect.colliderect(enemy_rect)


# This function shows a game over message on the screen
def draw_game_over(screen, font):
    # Create the text that will appear on the screen
    text = font.render("Game Over - Press R to Restart", True, (255, 255, 255))

    # Draw the text on the screen
    screen.blit(text, (120, 250))

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

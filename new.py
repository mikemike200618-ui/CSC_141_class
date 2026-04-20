
import pygame
import random
# Initialize Pygame
pygame.init()
# Set up the display
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Jumper Game")
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Player properties
player_width = 50
player_height = 50
player_x = 100
player_y = window_size[1] - player_height
player_velocity_y = 0
is_jumping = False
# Obstacle properties
obstacle_width = 50
obstacle_height = 50
obstacle_x = window_size[0]
obstacle_y = window_size[1] - obstacle_height
obstacle_velocity_x = 5
# Timer
start_time = pygame.time.get_ticks()
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                player_velocity_y = -15
                is_jumping = True
    # Update player position
    player_y += player_velocity_y
    if player_y >= window_size[1] - player_height:
        player_y = window_size[1] - player_height
        is_jumping = False
    else:
        player_velocity_y += 1  # Gravity effect
    # Update obstacle position
    obstacle_x -= obstacle_velocity_x
    if obstacle_x < -obstacle_width:
        obstacle_x = window_size[0]
        obstacle_y = window_size[1] - obstacle_height
    # Check for collision
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
    if player_rect.colliderect(obstacle_rect):
        print("Game Over!")
        running = False
    # Fill the background with white color
    screen.fill(WHITE)
    # Draw the player and the obstacle
    pygame.draw.rect(screen, BLACK, player_rect)
    pygame.draw.rect(screen, BLACK, obstacle_rect)
    # Display timer
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Convert to seconds
    font = pygame.font.SysFont(None, 36)
    timer_text = font.render(f"Time: {elapsed_time:.2f} seconds", True, BLACK)
    screen.blit(timer_text, (10, 10))
    # Update the display
    pygame.display.flip()  
# Quit Pygame
pygame.quit()   
obstacle_velocity_x = 10  # Change this value to slow down the obstacle speed 




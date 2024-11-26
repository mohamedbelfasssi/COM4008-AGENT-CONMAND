import pygame
import sys

# Initialize the game
pygame.init()

# Screen dimensions
width, height = 900, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Agent Command")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
CHARACTER_COLOR = (255, 100, 0)

# Clock settings
clock = pygame.time.Clock()
FPS = 60

# Player attributes
player_size = 40
agent_conmand = pygame.Rect(200, 500, player_size, player_size)
agent_speed = 10

# Level elements
prohibited_zones = [pygame.Rect(300, 400, 100, 50), pygame.Rect(500, 200, 100, 50)]
safe_zone = pygame.Rect(700, 500, 50, 50)

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement of character
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        agent_conmand.x -= agent_speed
    if keys[pygame.K_RIGHT]:
        agent_conmand.x += agent_speed
    if keys[pygame.K_DOWN]:
        agent_conmand.y += agent_speed
    if keys[pygame.K_UP]:
        agent_conmand.y -= agent_speed

    # Collision detection
    for zone in prohibited_zones:
        if agent_conmand.colliderect(zone):
            # Reset position if collided with prohibited zone
            agent_conmand.x, agent_conmand.y = 200, 500

    # Check if player reaches the safe zone
    if agent_conmand.colliderect(safe_zone):
        print("You have reached your goal, Congratulations!")
        running = False

    # Draw level elements
    pygame.draw.rect(screen, GREEN, safe_zone)
    for zone in prohibited_zones:
        pygame.draw.rect(screen, RED, zone)

    # Draw player
    pygame.draw.rect(screen, CHARACTER_COLOR, agent_conmand)

    # Update screen
    pygame.display.flip()
    clock.tick(FPS)

# Quit game
pygame.quit()
sys.exit()

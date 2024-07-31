import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPACESHIP_WIDTH = 60
SPACESHIP_HEIGHT = 50
SPACESHIP_COLOR = (0, 128, 255)  # Blue color
BULLET_WIDTH = 5
BULLET_HEIGHT = 10
BULLET_COLOR = (255, 0, 0)  # Red color
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 50
ENEMY_COLOR = (0, 255, 0)  # Green color
BOSS_WIDTH = 100
BOSS_HEIGHT = 100
BOSS_COLOR = (255, 255, 255)  # White color
BACKGROUND_COLOR = (0, 0, 0)  # Black color
SPACESHIP_SPEED = 7
BULLET_SPEED = 10
ENEMY_SPEED = 5
BOSS_SPEED = 5
ENEMY_INTERVAL = 2000  # Time in milliseconds for enemy spawning
BOSS_HEALTH_INCREMENT = 5

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Shooter Game')

# Load fonts
font = pygame.font.Font(None, 36)

def draw_spaceship(x, y):
    pygame.draw.rect(screen, SPACESHIP_COLOR, (x, y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

def draw_bullet(x, y):
    pygame.draw.rect(screen, BULLET_COLOR, (x, y, BULLET_WIDTH, BULLET_HEIGHT))

def draw_enemy(x, y):
    pygame.draw.rect(screen, ENEMY_COLOR, (x, y, ENEMY_WIDTH, ENEMY_HEIGHT))

def draw_boss(x, y, health):
    pygame.draw.rect(screen, BOSS_COLOR, (x, y, BOSS_WIDTH, BOSS_HEIGHT))
    health_surface = font.render(f'Health: {health}', True, (255, 0, 0))
    screen.blit(health_surface, (x, y - 30))

def draw_level(level):
    level_surface = font.render(f'Level: {level}', True, (255, 255, 255))
    screen.blit(level_surface, (10, 10))

def draw_text(text, size, color, position):
    font = pygame.font.Font(None, size)
    surface = font.render(text, True, color)
    screen.blit(surface, position)

def show_level_cleared(level):
    screen.fill(BACKGROUND_COLOR)
    draw_text(f'Level {level} Cleared!', 48, (0, 255, 0), (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 30))
    pygame.display.flip()
    pygame.time.wait(2000)  # Wait for 2 seconds before continuing

def main():
    global ENEMY_INTERVAL  # Declare ENEMY_INTERVAL as global
    spaceship_x = SCREEN_WIDTH // 2 - SPACESHIP_WIDTH // 2
    spaceship_y = SCREEN_HEIGHT - SPACESHIP_HEIGHT - 10
    bullets = []
    enemies = []
    boss = None
    score = 0
    level = 1
    boss_health = BOSS_HEALTH_INCREMENT * level
    boss_active = False
    last_enemy_spawn_time = pygame.time.get_ticks()
    last_boss_spawn_time = pygame.time.get_ticks()
    shoot_cooldown = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            spaceship_x -= SPACESHIP_SPEED
        if keys[pygame.K_RIGHT]:
            spaceship_x += SPACESHIP_SPEED
        if keys[pygame.K_SPACE] and shoot_cooldown == 0:
            bullets.append([spaceship_x + SPACESHIP_WIDTH // 2 - BULLET_WIDTH // 2, spaceship_y])
            shoot_cooldown = 10  # Adjust the cooldown to control the rate of fire

        # Keep spaceship within the screen bounds
        spaceship_x = max(0, min(SCREEN_WIDTH - SPACESHIP_WIDTH, spaceship_x))

        current_time = pygame.time.get_ticks()

        # Spawn enemies
        if not boss_active and current_time - last_enemy_spawn_time > ENEMY_INTERVAL:
            enemy_x = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
            enemy_y = -ENEMY_HEIGHT
            enemies.append([enemy_x, enemy_y])
            last_enemy_spawn_time = current_time

        # Check if level should be cleared
        if score >= 10 * level and not boss_active:
            # Start boss fight
            boss_x = SCREEN_WIDTH // 2 - BOSS_WIDTH // 2
            boss_y = -BOSS_HEIGHT
            boss = [boss_x, boss_y, boss_health]
            boss_active = True
            last_boss_spawn_time = current_time

        # Update enemy positions
        enemies = [[ex, ey + ENEMY_SPEED] for ex, ey in enemies if ey < SCREEN_HEIGHT]

        # Update bullet positions
        bullets = [[bx, by - BULLET_SPEED] for bx, by in bullets if by > 0]

        # Check bullet collisions with enemies
        for bx, by in bullets:
            for ex, ey in enemies:
                if pygame.Rect(bx, by, BULLET_WIDTH, BULLET_HEIGHT).colliderect(pygame.Rect(ex, ey, ENEMY_WIDTH, ENEMY_HEIGHT)):
                    enemies.remove([ex, ey])
                    bullets.remove([bx, by])
                    score += 1
                    print(f"Enemy hit! Score: {score}")  # Debug: Check bullet-enemy collisions
                    break

        # Check if the spaceship collides with any enemies
        for ex, ey in enemies:
            if pygame.Rect(spaceship_x, spaceship_y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT).colliderect(pygame.Rect(ex, ey, ENEMY_WIDTH, ENEMY_HEIGHT)):
                print("Game Over: Spaceship collided with enemy!")
                pygame.quit()
                sys.exit()

        # Check if the boss is active
        if boss_active:
            bx_boss, by_boss, boss_health = boss
            # Move the boss to follow the spaceship
            if spaceship_x < bx_boss:
                bx_boss -= BOSS_SPEED
            elif spaceship_x > bx_boss:
                bx_boss += BOSS_SPEED
            by_boss += BOSS_SPEED

            if pygame.Rect(bx_boss, by_boss, BOSS_WIDTH, BOSS_HEIGHT).colliderect(pygame.Rect(spaceship_x, spaceship_y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)):
                print("Game Over: Boss touched the spaceship!")
                pygame.quit()
                sys.exit()

            for bx, by in bullets:
                if pygame.Rect(bx, by, BULLET_WIDTH, BULLET_HEIGHT).colliderect(pygame.Rect(bx_boss, by_boss, BOSS_WIDTH, BOSS_HEIGHT)):
                    boss_health -= 1
                    bullets.remove([bx, by])
                    print(f"Boss hit! Boss Health: {boss_health}")  # Debug: Check bullet-boss collisions
                    if boss_health <= 0:
                        boss = None
                        boss_active = False
                        score += 1
                        ENEMY_INTERVAL = max(1000, ENEMY_INTERVAL - 100)  # Speed up enemy spawn
                        show_level_cleared(level)
                        level += 1
                        enemies = []  # Clear enemies for the new level
                        boss_health = BOSS_HEALTH_INCREMENT * level
                    else:
                        boss[2] = boss_health  # Update boss health
                    break

        # Decrease shoot cooldown
        if shoot_cooldown > 0:
            shoot_cooldown -= 1

        # Drawing
        screen.fill(BACKGROUND_COLOR)
        for bx, by in bullets:
            draw_bullet(bx, by)
        for ex, ey in enemies:
            draw_enemy(ex, ey)
        if boss:
            bx_boss, by_boss, boss_health = boss
            print(f"Boss Position: ({bx_boss}, {by_boss})")  # Debug: Check boss position
            draw_boss(bx_boss, by_boss, boss_health)
        draw_spaceship(spaceship_x, spaceship_y)
        draw_level(level)
        score_surface = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_surface, (10, 50))
        pygame.display.flip()
        pygame.time.Clock().tick(30)

if __name__ == '__main__':
    main()

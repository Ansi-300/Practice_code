import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game variables
gravity = 0.30
bird_movement = 0
score = 0
high_score = 0
game_active = True

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# Load assets
bird_surface = pygame.Surface((40, 40))
bird_surface.fill(BLUE)
bird_rect = bird_surface.get_rect(center=(100, SCREEN_HEIGHT // 2))

pipe_surface = pygame.Surface((50, 300))
pipe_surface.fill(GREEN)
pipe_list = []

# Timer for spawning pipes
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

# Font for score display
font = pygame.font.Font(None, 36)

def draw_score(score):
    score_surface = font.render(f"Score: {int(score)}", True, WHITE)
    score_rect = score_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))
    screen.blit(score_surface, score_rect)

def draw_high_score(high_score):
    high_score_surface = font.render(f"High Score: {int(high_score)}", True, WHITE)
    high_score_rect = high_score_surface.get_rect(center=(SCREEN_WIDTH // 2, 100))
    screen.blit(high_score_surface, high_score_rect)

def create_pipe():
    random_pipe_pos = random.randint(200, 400)
    bottom_pipe = pipe_surface.get_rect(midtop=(500, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(500, random_pipe_pos - 150))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 3
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= SCREEN_HEIGHT:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

def check_collisions(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False

    if bird_rect.top <= -50 or bird_rect.bottom >= SCREEN_HEIGHT:
        return False

    return True

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = -6

            if event.key == pygame.K_SPACE and not game_active:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, SCREEN_HEIGHT // 2)
                bird_movement = 0
                score = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    screen.fill(BLACK)

    if game_active:
        # Bird movement
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird_surface, bird_rect)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        # Collision detection
        game_active = check_collisions(pipe_list)

        # Score
        score += 0.01
        draw_score(score)
    else:
        # Game over screen
        draw_score(score)
        draw_high_score(high_score)
        if score > high_score:
            high_score = score

    pygame.display.update()
    clock.tick(120)
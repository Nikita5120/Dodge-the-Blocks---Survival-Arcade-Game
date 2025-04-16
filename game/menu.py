import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT

def draw_text(screen, text, size, y_offset):
    font = pygame.font.SysFont("Arial", size)
    text_surface = font.render(text, True, (0, 0, 0))
    rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + y_offset))
    screen.blit(text_surface, rect)

def start_menu(screen):
    waiting = True
    while waiting:
        screen.fill((255, 255, 255))
        draw_text(screen, "DODGE THE BLOCKS", 40, -60)
        draw_text(screen, "Press ENTER to Start", 30, 0)
        draw_text(screen, "Press ESC to Quit", 25, 40)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

def game_over_menu(screen, score):
    font = pygame.font.SysFont("Arial", 36)
    game_over_text = font.render(f"Game Over! Final Score: {score}", True, (0, 0, 0))
    restart_text = font.render("Press R to Restart or Q to Quit", True, (0, 0, 0))
    
    screen.fill((255, 255, 255))
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 40))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 20))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart
                    return True
                if event.key == pygame.K_q:  # Quit
                    return False

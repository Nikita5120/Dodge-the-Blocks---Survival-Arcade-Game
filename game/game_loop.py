import pygame
import random
from game.player import Player
from game.block import Block
from config import *
import os
from game.menu import start_menu, game_over_menu
from utils import load_high_score, save_high_score

pygame.mixer.init()

# Load sounds
pygame.mixer.music.load(os.path.join("assets", "sounds", "background.mp3"))
pygame.mixer.music.play(-1)  # Loop forever
gameover_sound = pygame.mixer.Sound(os.path.join("assets", "sounds", "gameover.wav"))

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # ✅ Moved above
    pygame.display.set_caption("Dodge the Blocks")
    start_menu(screen)  # ✅ Now screen is initialized

    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 24)

    high_score = load_high_score()  # Load the high score from file

    while True:
        player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - PLAYER_SIZE - 10, PLAYER_SIZE, PLAYER_SPEED)
        blocks = []
        block_speed = INITIAL_BLOCK_SPEED
        score = 0
        running = True

        pygame.mixer.music.play(-1)  # Restart background music

        while running:
            screen.fill((255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            keys = pygame.key.get_pressed()
            player.move(keys, SCREEN_WIDTH)

            if random.randint(1, 30) == 1:
                blocks.append(Block(SCREEN_WIDTH, BLOCK_SIZE, block_speed))

            for block in blocks[:]:
                block.move()
                block.draw(screen)
                if block.rect.colliderect(player.rect):
                    pygame.mixer.music.stop()
                    gameover_sound.play()
                    running = False
                if block.rect.top > SCREEN_HEIGHT:
                    blocks.remove(block)
                    score += 1
                    if score % 5 == 0:
                        block_speed += 0.5

            player.draw(screen)

            # Display Score and High Score
            score_text = font.render(f"Score: {score}", True, (0, 0, 0))
            high_score_text = font.render(f"High Score: {high_score}", True, (0, 0, 0))
            screen.blit(score_text, (10, 10))
            screen.blit(high_score_text, (10, 40))

            pygame.display.flip()
            clock.tick(FPS)

        # Save new high score if applicable
        if score > high_score:
            high_score = score
            save_high_score(high_score)

        # Game Over Menu with restart option
        restart = game_over_menu(screen, score)
        if not restart:
            break

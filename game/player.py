import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, size, speed):
        super().__init__()

        # Load player image and get rectangle
        self.image = pygame.image.load('assets/images/player.png')
        self.image = pygame.transform.scale(self.image, (size, size))  # Resize image to the correct size
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed

    def move(self, keys, screen_width):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

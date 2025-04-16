import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, x, size, speed):
        super().__init__()

        # Load block image and get rectangle
        self.image = pygame.image.load('assets/images/block.png')
        self.image = pygame.transform.scale(self.image, (size, size))  # Resize image to the correct size
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = -size  # Start the block above the screen
        self.speed = speed

    def move(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

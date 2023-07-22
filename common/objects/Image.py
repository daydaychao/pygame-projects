import pygame

class Image:
    def __init__(self, image_path, x=50, y=50 , width=100, height=100):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = width
        self.rect.height = height
        self.width = width
        self.height = height

    def setXY(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        scaled_image = pygame.transform.scale(self.image, (self.width, self.height))
        screen.blit(scaled_image, self.rect)

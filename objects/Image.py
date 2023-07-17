import pygame

class Image:    
    def __init__(self, image_path, x=0, y=0):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y

    def setXY(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        print(self.rect)
        screen.blit(self.image, self.rect)

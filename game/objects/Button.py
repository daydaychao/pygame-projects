import pygame

class Button:
    def __init__(self, image_path, position):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = position

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def check_collision(self, point):
        return self.rect.collidepoint(point)

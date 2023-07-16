import pygame

class Text:
    def __init__(self, font_path, font_size, text, color, position):
        self.font = pygame.font.Font(font_path, font_size)
        self.text = text
        self.color = color
        self.position = position
        self.rendered_text = self.font.render(text, True, color)
        self.rect = self.rendered_text.get_rect()
        self.rect.center = position

    def set_text(self, text):
        self.text = text
        self.rendered_text = self.font.render(text, True, self.color)
        self.rect = self.rendered_text.get_rect()
        self.rect.center = self.position

    def draw(self, surface):
        surface.blit(self.rendered_text, self.rect)

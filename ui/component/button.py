import pygame

class Button():
    def __init__(self, screen, font, word_color, pos, size, color = "silver", text = "button"):
        width, height = size
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = pos
        pygame.draw.rect(screen, color, self.rect)
        word = font.render(text, True, word_color)
        word_rect = word.get_rect(center = self.rect.center)
        screen.blit(word, word_rect)
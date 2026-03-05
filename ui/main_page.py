import pygame
import os


class Main_page():
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont(None, 36)
        self.screen_height = 600
        self.screen_width = 900
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen.fill("silver")
        
        #self.create_button((int(self.screen_width/2), int(self.screen_height/2), 90, 60), text="sort_algo")
        self.sort_button_center = (int(self.screen_width/2), int(self.screen_height/2))
        self.sort_button_size = (90, 60)
        
        self.run = True
        self.clock = pygame.time.Clock()
        while self.run:
            self.mouse_pos = pygame.mouse.get_pos()
            if hasattr(self, "sort_button") and self.sort_button.rect.collidepoint(self.mouse_pos):
                color = (30, 144, 255) #dodgerblue
            else:
                color = (255, 255, 255) #white
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
            
            self.sort_button = Button(self.screen, self.font, color,
                                      self.sort_button_center, 
                                      self.sort_button_size, 
                                      text = "sort algo")
            self.clock.tick(30)
            pygame.display.update()
    def quit(self):
        self.run = False
        
class Button():
    def __init__(self, screen, font, word_color, pos, size, color = "silver", text = "button"):
        width, height = size
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = pos
        pygame.draw.rect(screen, color, self.rect)
        word = font.render(text, True, word_color)
        word_rect = word.get_rect(center = self.rect.center)
        screen.blit(word, word_rect)
        
                
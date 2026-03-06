import pygame
import os
from ui.component.button import Button

class Sort_page():
    def __init__(self, page_manager):
        self.font = pygame.font.SysFont(None, 36)
        self.next_page = None
        self.page_manager = page_manager
    def draw(self, screen):
        screen.fill("silver")
        self.back_button_center = (40, 20)
        self.back_button_size = (50, 30)
        self.mouse_pos = pygame.mouse.get_pos()
        if hasattr(self, "back_button") and self.back_button.rect.collidepoint(self.mouse_pos):
            back_color = (30, 144, 255) #dodgerblue
        else:
            back_color = (255, 255, 255) #white
        self.back_button = Button(screen, self.font, back_color,
                                  self.back_button_center,
                                  self.back_button_size,
                                  text= "Back")
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.back_button.rect.collidepoint(event.pos):
                self.next_page = self.page_manager.switch_page("main")
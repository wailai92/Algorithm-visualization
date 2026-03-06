import pygame
import os
from ui.component.button import Button

class Main_page():
    def __init__(self, page_manager):
        self.font = pygame.font.SysFont(None, 36)
        self.next_page = None
        self.page_manager = page_manager
    def draw(self, screen):
        screen.fill("black")
        self.sort_button_center = (int(screen.get_width() / 2), int(screen.get_height() / 3))
        self.sort_button_size = (110, 30)
        self.graph_button_center = (int(screen.get_width() / 2), int(screen.get_height() / 2))
        self.graph_button_size = (130, 30)
        self.setting_button_center = (int(screen.get_width() / 2), int(2 * screen.get_height() / 3))
        self.setting_button_size = (100, 30)
        
        self.mouse_pos = pygame.mouse.get_pos()
        if hasattr(self, "sort_button") and self.sort_button.rect.collidepoint(self.mouse_pos):
            sort_color = (30, 144, 255) #dodgerblue
        else:
            sort_color = (255, 255, 255) #white
        if hasattr(self, "graph_button") and self.graph_button.rect.collidepoint(self.mouse_pos):
            graph_color = (30, 144, 255) #dodgerblue
        else:
            graph_color = (255, 255, 255) #white
        if hasattr(self, "setting_button") and self.setting_button.rect.collidepoint(self.mouse_pos):
            setting_color = (30, 144, 255) #dodgerblue
        else:
            setting_color = (255, 255, 255) #white
                    
        self.sort_button = Button(screen, self.font, sort_color,
                                    self.sort_button_center, 
                                    self.sort_button_size, 
                                    text = "sort algo")
            
        self.graph_button = Button(screen, self.font, graph_color,
                                    self.graph_button_center,
                                    self.graph_button_size,
                                    text = "graph algo")
        
        self.setting_button = Button(screen, self.font, setting_color,
                                        self.setting_button_center, 
                                        self.setting_button_size, 
                                        text = "setting")
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.sort_button.rect.collidepoint(event.pos):
                self.next_page = self.page_manager.switch_page("sort")
            elif self.graph_button.rect.collidepoint(event.pos):
                self.next_page = self.page_manager.switch_page("graph")
            elif self.setting_button.rect.collidepoint(event.pos):
                self.next_page = self.page_manager.switch_page("setting")
        
        
                
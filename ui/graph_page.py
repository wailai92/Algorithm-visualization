import pygame
import os
from ui.component.button import Button
from ui.component.button_list import Button_list
from core.algorithm_manager import Algorithm_manager
from core.path_manager import Path_manager

class Graph_page():
    def __init__(self, page_manager):
        self.font = pygame.font.SysFont(None, 36)
        self.next_page = None
        self.page_manager = page_manager
        self.path_manager = Path_manager()
        self.algorithm_manager = Algorithm_manager(self.path_manager)
    def draw(self, screen):
        width, height = screen.get_size()
        left_width = 250
        right_width = width - left_width
        top_right_height = (6 * height / 7)
        bottom_right_height = height - top_right_height
        top_left_height = 35
        bottom_left_height = height - top_left_height
        
        top_left_rect = pygame.Rect(0, 0, left_width, top_left_height)
        bottom_left_rect = pygame.Rect(0, top_left_height, left_width, bottom_left_height)
        top_right_rect = pygame.Rect(left_width, 0, right_width, top_right_height)
        bottom_right_rect = pygame.Rect(left_width, top_right_height, right_width, bottom_right_height)
        
        pygame.draw.rect(screen, (0, 0, 0), top_left_rect) #black
        pygame.draw.rect(screen, (40, 40, 40), bottom_left_rect) #dark gray
        pygame.draw.rect(screen, (192, 192, 192), top_right_rect) #silver
        pygame.draw.rect(screen, (255, 255, 255), bottom_right_rect) #white
        #screen.fill("black")
        #self.back_button_center = (40, 20)
        self.back_button_size = (250, 35)
        
        self.graph_algo = self.algorithm_manager.get_graph_algo_name()
        self.algo_button_list_size = (left_width, 30)
        self.algo_button_list_color = []
        
        self.mouse_pos = pygame.mouse.get_pos()
        if hasattr(self, "back_button") and self.back_button.rect.collidepoint(self.mouse_pos):
            back_color = (30, 144, 255) #dodgerblue
        else:
            back_color = (255, 255, 255) #white
        self.back_button = Button(screen, self.font, back_color,
                                  (0, 0),
                                  self.back_button_size,
                                  text= "Back", center= False)
        for i in range(len(self.graph_algo)):
            if hasattr(self, "algo_button_list") and self.algo_button_list.button[i].rect.collidepoint(self.mouse_pos):
                self.algo_button_list_color.append((30, 144, 255))
            else:
                self.algo_button_list_color.append((255, 255, 255))
        self.algo_button_list = Button_list(screen, self.graph_algo, 
                                            (0, 40), self.algo_button_list_size,
                                            (40, 40, 40), self.font,
                                            self.algo_button_list_color)
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.back_button.rect.collidepoint(event.pos):
                self.next_page = self.page_manager.switch_page("main")
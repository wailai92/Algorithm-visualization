import pygame
import os
from ui.component.button import Button
from ui.component.button_list import Button_list
from core.algorithm_manager import Algorithm_manager
from core.path_manager import Path_manager
from core.visualizer.sorting_visualizer import Sorting_visualizer

class Sort_page():
    def __init__(self, page_manager):
        self.font = pygame.font.SysFont(None, 36)
        self.next_page = None
        self.page_manager = page_manager
        self.path_manager = Path_manager()
        self.algorithm_manager = Algorithm_manager(self.path_manager)
        self.sorting_visualizer = Sorting_visualizer()
        self.chosen_algo_name = ""
        self.chosen_algo = None
        self.if_init_visualizer = False
        self.left_width = 20
        self.graph_set_screen = False
        
    def draw(self, screen):
        width, height = screen.get_size()
        right_width = width - self.left_width
        top_right_height = (6 * height // 7)
        bottom_right_height = height - top_right_height
        top_left_height = 35
        bottom_left_height = height - top_left_height
        
        top_left_rect = pygame.Rect(0, 0, self.left_width, top_left_height)
        bottom_left_rect = pygame.Rect(0, top_left_height, self.left_width, bottom_left_height)
        top_right_rect = pygame.Rect(self.left_width, 0, right_width, top_right_height)
        bottom_right_rect = pygame.Rect(self.left_width, top_right_height, right_width, bottom_right_height)
        left_full_rect = pygame.Rect(0, 0, self.left_width, height)
        
        pygame.draw.rect(screen, (192, 192, 192), top_right_rect) #silver
        pygame.draw.rect(screen, (255, 255, 255), bottom_right_rect) #white
        #screen.fill("black")
        #self.back_button_center = (40, 20)
        if self.graph_set_screen:
            self.sorting_visualizer.set_screen(screen, top_right_rect, bottom_right_rect)
            self.graph_set_screen = False
        if self.left_width == 200:
            pygame.draw.rect(screen, (0, 0, 0), top_left_rect) #black
            pygame.draw.rect(screen, (40, 40, 40), bottom_left_rect) #dark gray
            
            self.sort_algo = self.algorithm_manager.get_sort_algo_name()
            self.algo_button_list_color = []
            
            self.mouse_pos = pygame.mouse.get_pos()
            local_pos = (self.mouse_pos[0], self.mouse_pos[1])
            if hasattr(self, "back_button") and self.back_button.rect.collidepoint(local_pos):
                back_color = (30, 144, 255) #dodgerblue
            else:
                back_color = (255, 255, 255) #white
            self.top_left_subsurface = screen.subsurface(top_left_rect)
            width = self.top_left_subsurface.get_width()
            height = self.top_left_subsurface.get_height()
            self.back_button_size = (width, height)
            self.back_button = Button(self.top_left_subsurface, self.font, back_color,
                                    (0, 0),
                                    self.back_button_size,
                                    text= "Back", center= False)
            local_pos = (self.mouse_pos[0], self.mouse_pos[1] - self.top_left_subsurface.get_height())
            for i in range(len(self.sort_algo)):
                if hasattr(self, "algo_button_list") and self.algo_button_list.button[i].rect.collidepoint(local_pos):
                    self.algo_button_list_color.append((30, 144, 255))
                else:
                    self.algo_button_list_color.append((255, 255, 255))
            self.bottom_left_subsurface = screen.subsurface(bottom_left_rect)
            width = self.bottom_left_subsurface.get_width()
            height = self.bottom_left_subsurface.get_height() #/ len(self.sort_algo)
            self.algo_button_list_size = (width, 35)
            self.algo_button_list = Button_list(self.bottom_left_subsurface, self.sort_algo, 
                                                (0, 0), self.algo_button_list_size,
                                                (40, 40, 40), self.font,
                                                self.algo_button_list_color)
            if self.mouse_pos[0] > self.left_width:
                self.left_width = 20
                self.graph_set_screen = True
                
        elif self.left_width == 20:
            pygame.draw.rect(screen, (40, 40, 40), left_full_rect) #dark gray
            self.left_full_subgraph = screen.subsurface(left_full_rect)
            
            center = self.left_full_subgraph.get_rect().center
            cx, cy = center
            size = 4  
            points = [
                (cx - size, cy - size),   
                (cx - size, cy + size),   
                (cx + size, cy)           
            ]
            pygame.draw.polygon(self.left_full_subgraph, (255, 255, 255), points)
            
            self.mouse_pos = pygame.mouse.get_pos()
            if self.mouse_pos[0] < self.left_width:
                self.left_width = 200
                self.graph_set_screen = True
                
        
        if self.if_init_visualizer:
            self.if_init_visualizer = False
            self.sorting_visualizer.init(self.chosen_algo, 200, screen, top_right_rect, bottom_right_rect)
        if self.chosen_algo:
            self.sorting_visualizer.draw()
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            local_pos = (event.pos[0], event.pos[1])
            if self.back_button.rect.collidepoint(local_pos):
                self.next_page = self.page_manager.switch_page("main")
                return
            local_pos = (event.pos[0], event.pos[1] - self.top_left_subsurface.get_height())
            for button in self.algo_button_list.button:
                if button.rect.collidepoint(local_pos):
                    self.chosen_algo_name = button.name
                    self.chosen_algo = self.algorithm_manager.get_algo("sort", button.name)
                    self.if_init_visualizer = True
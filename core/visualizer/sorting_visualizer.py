import pygame
import random
class Sorting_visualizer():
    def __init__(self):
        self.data_list = []
        self.color_list = []
        self.data_length = 0
        self.generator = None
        self.pause = True
        self.data_length = 0
        self.screen = None
        self.chart_surface = None #screen.subsurface(top_rect)
        self.operation_surface = None #screen.subsurface(bottom_rect)
        self.step_delay = 30
        self.last_step_time = 0
        #self.finished = True
    def status_decode(self, status):
        if status["type"] == "compare":
            self.color_list[status["first"]] = (255, 0, 0) #red
            self.color_list[status["second"]] = (255, 0, 0) #red
        elif status["type"] == "swap":
            i = status["first"]
            j = status["second"]
            #self.status_decode(next(self.generator))
            #self.data_list[i], self.data_list[j] = self.data_list[j], self.data_list[i]
        elif status["type"] == "finished_cut":
            self.color_list[self.data_length - status["index"] - 1] = "magenta" #black
            self.status_decode(next(self.generator))
        elif status["type"] == "early_finished" :
            self.color_list = ["magenta" for _ in range(self.data_length)]
            self.pause = True
            #self.finished = True
        elif status["type"] == "finished":
            self.color_list = ["magenta" for _ in range(self.data_length)]
            self.pause = True
            #self.finished = True
            
    def draw(self):
        self.chart_surface.fill((192, 192, 192))
        top_width = self.chart_surface.get_width()
        top_height = self.chart_surface.get_height()
        gap = 2
        usable_height = top_height - 10

        bar_width = max(1, top_width // self.data_length - gap)

        total_bars_width = self.data_length * bar_width + (self.data_length - 1) * gap

        start_x = (top_width - total_bars_width) // 2

        max_val = max(self.data_list)

        for index, value in enumerate(self.data_list):
            bar_height = usable_height * value / max_val
            x = start_x + index * (bar_width + gap)
            y = top_height - bar_height

            rect = pygame.Rect(x, y, bar_width, bar_height)
            pygame.draw.rect(self.chart_surface, self.color_list[index], rect)
            #pygame.draw.rect(self.chart_surface, (0, 0, 0), rect, 1)
            
        
        self.operation_surface.fill((255, 255, 255))
        bottom_width = self.operation_surface.get_width()
        bottom_height = self.operation_surface.get_height()   
        #operation button set...
        
        self.reset_active_color()
        if not self.pause:
            try:
                status = next(self.generator)
                self.status_decode(status)
            except StopIteration:
                self.pause = True

    def reset_active_color(self):
        for i in range(self.data_length):
            if self.color_list[i] != "magenta": 
                self.color_list[i] = (0, 150, 255)
        
    def set_data_length(self, length):
        self.data_length = length
    def init_data_list(self):
        self.data_list = [random.randint(10, 400) for _ in range(self.data_length)]
        self.data_length = self.data_length
        self.init_color_list()
    def init_color_list(self):
        self.color_list = [(0, 150, 255) for _ in range(self.data_length)] 
    def set_generator(self, algo_function):
        self.generator = algo_function(self.data_list)
    def set_pause(self):
        self.pause = True
    def set_screen(self, screen, top_rect, bottom_rect):
        self.screen = screen
        self.chart_surface = screen.subsurface(top_rect)
        self.operation_surface = screen.subsurface(bottom_rect)
    def init(self, algo_function, length, screen, top_rect, bottom_rect):
        if not algo_function:
            return
        self.set_data_length(length)
        self.init_data_list()
        self.init_color_list()
        self.set_generator(algo_function)
        self.set_screen(screen, top_rect, bottom_rect)
        self.set_pause()
        self.pause = False
    def inverse_pause(self):
        self.pause = not self.pause
        
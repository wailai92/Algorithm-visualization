import pygame
from ui.component.button import Button
class Pull_list():
    def __init__(self, pos, size, options, font):
        self.pos = pos
        self.size = size
        self.options = options
        self.font = font
        self.expand = False
        self.selected_index = 0
    def get_selected_text(self):
        return self.options[self.selected_index]
    def draw(self, screen):
        temp = 0
    def handle_event(self, event):
        temp = 0
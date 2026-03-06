from ui.main_page import Main_page
from ui.sort_page import Sort_page
from ui.page_manager import Page_manager
import sys
import pygame

def main():
    pygame.init()
    screen_height = 600
    screen_width = 900
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    page_manager = Page_manager()
    current_page = Main_page(page_manager)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            current_page.handle_event(event)
        if current_page.next_page is not None:
            current_page = current_page.next_page
        current_page.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        
if __name__ == "__main__":
    main()
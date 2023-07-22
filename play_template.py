import pygame
import os
from common.objects.Image import Image
from common.objects.Text import Text
from common.objects.Button import Button


def main():

    # 取得目前檔案所在目錄
    current_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(current_dir, 'game02_get_gold/images')
    fonts_dir = os.path.join(current_dir, 'common/fonts')
    font_path = fonts_dir+'/NotoSansTC-Regular.otf'

    # Setup
    window_width = 1280
    window_height = 720
    center_x = window_width / 2
    center_y = window_height / 2
    running = True
    dt = 0
    pygame.init()

    screen = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()

    # Event Handlers

    def handle_quit_event():
        global running
        running = False
        pygame.quit()

    # Events
    event_handlers = {
        pygame.QUIT: handle_quit_event,
    }

    # Game Loop
    while running:
        for event in pygame.event.get():
            if event.type in event_handlers:
                event_handlers[event.type]()

        screen.fill("gray")

        # Logic

        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()

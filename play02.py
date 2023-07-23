import pygame
import os
import random
from common.objects.Image import Image
from common.objects.Text import Text
from common.objects.Button import Button
from game02_get_gold.config import AUDIO_PATHS, IMAGE_PATHS, SCREENSIZE, BACKGROUND_COLOR, HIGHEST_SCORE_RECORD_FILEPATH, FONT_PATH, FPS
from game02_get_gold.modules.hero import Hero


def playbgm():
    pygame.mixer.music.load(AUDIO_PATHS['bgm'])
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.25)


def main():
    # Setup
    window_width = SCREENSIZE[0]
    window_height = SCREENSIZE[1]
    center_x = window_width / 2
    center_y = window_height / 2
    running = True
    dt = 0

    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("左右跑跑接東西")
    screen = pygame.display.set_mode((window_width, window_height))

    # Event Handlers
    def handle_quit_event():
        global running
        running = False
        pygame.quit()

    # Events
    event_handlers = {
        pygame.QUIT: handle_quit_event,
    }

    # Start
    playbgm()
    bg = Image(IMAGE_PATHS['background'], 0,
               0, SCREENSIZE[0], SCREENSIZE[1])

    hero = Hero(IMAGE_PATHS['hero'], position=(375, 520))
    food_sprites_group = pygame.sprite.Group()
    generate_food_freq = random.randint(10, 20)
    generate_food_count = 0
    score = 0
    highest_score = 0 if not os.path.exists(HIGHEST_SCORE_RECORD_FILEPATH) else int(
        open(HIGHEST_SCORE_RECORD_FILEPATH).read())

    countdown_text = Text(FONT_PATH, 24, '', (0, 0, 0), (SCREENSIZE[0]-30, 5))

    # Game Loop
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type in event_handlers:
                event_handlers[event.type]()

        # BG
        screen.fill(0)
        bg.draw(screen)

        # Hero
        hero.draw(screen)

        # Count Down
        countdown_seconds = (90000 - pygame.time.get_ticks()) // 1000
        minutes = countdown_seconds // 60
        seconds = countdown_seconds % 60
        countdown_text.set_text(f'Count down: {minutes}:{seconds:02}')
        countdown_text.draw(screen, align='right')

        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()

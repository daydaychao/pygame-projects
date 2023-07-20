import pygame

from defs.get_weather_handler import get_weather_data
from defs.input_handler import handle_input

from objects.Button import Button
from objects.Text import Text
from objects.Image import Image


def render_weather_data():  # 取得天氣資料
    global title, temperature, rain, description
    title, temperature, rain, description = get_weather_data()


def main():

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
        pygame.quit()

    def handle_button_click():
        if button.check_collision(pygame.mouse.get_pos()):
            text.set_text("Lalala")  # 当按钮与鼠标点击位置发生碰撞时执行相应逻辑

    # Events
    event_handlers = {
        pygame.QUIT: handle_quit_event,
        pygame.MOUSEBUTTONDOWN: handle_button_click
    }

    # Game Created
    logo_image = Image("images/pygame_lofi.png", center_x, -100, 40, 80)
    button = Button("images/button.png", (center_x, window_height - 100))
    text = Text(None, 36, "AAA",  (255, 255, 255), (center_x, 20))
    player_pos = pygame.Vector2(center_x, center_y)
    screen.fill("gray")

    path = 'fonts/NotoSansTC-Regular.otf'
    titleText = Text(path, 24, '地區:'+title,  (255, 255, 255), (20, 20))
    descriptionText = Text(path, 24, '溫度:'+description,
                           (255, 255, 255), (20, 50))
    rainText = Text(path, 24, '降雨機率:'+rain,  (255, 255, 255), (20, 80))
    temperatureText = Text(path, 24, '天氣狀況:'+temperature,
                           (255, 255, 255), (20, 110))

    # Game Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type in event_handlers:
                event_handlers[event.type]()

        # 更新gray
        screen.fill("black")
        button.draw(screen)
        text.draw(screen)
        logo_image.draw(screen)

        titleText.draw(screen, 'left')
        descriptionText.draw(screen, 'left')
        rainText.draw(screen, 'left')
        temperatureText.draw(screen, 'left')

        # 移動
        handle_input(player_pos, dt)
        pygame.draw.circle(screen, "yellow", player_pos, 40)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    render_weather_data()
    main()
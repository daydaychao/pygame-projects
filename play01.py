
import pygame
import os
from common.objects.Image import Image
from common.objects.Text import Text
from common.objects.Button import Button
from game01_weather.defs.input_handler import handle_input
from game01_weather.defs.get_weather_handler import get_weather_data


def render_weather_data():  # 取得天氣資料
    global title, temperature, rain, description
    title, temperature, rain, description = get_weather_data()


def main():

    # 取得目前檔案所在目錄
    current_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(current_dir, 'game01_weather/images')
    fonts_dir = os.path.join(current_dir, 'common/fonts')

    # Setup
    running = True
    window_width = 1280
    window_height = 720
    center_x = window_width / 2
    center_y = window_height / 2
    dt = 0
    pygame.init()

    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("抓取高雄天氣")
    clock = pygame.time.Clock()

    # Event Handlers

    def handle_quit_event():
        global running
        running = False
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
    logo_image = Image(images_dir+"/pygame_lofi.png", center_x, -100, 40, 80)
    button = Button(images_dir+"/button.png", (center_x, window_height - 100))
    text = Text(None, 36, "AAA",  (255, 255, 255), (center_x, 20))
    player_pos = pygame.Vector2(center_x, center_y)
    screen.fill("gray")

    font_path = fonts_dir+'/NotoSansTC-Regular.otf'
    titleText = Text(font_path, 24, '地區:'+title,  (255, 255, 255), (20, 20))
    descriptionText = Text(font_path, 24, '溫度:'+description,
                           (255, 255, 255), (20, 50))
    rainText = Text(font_path, 24, '降雨機率:'+rain,  (255, 255, 255), (20, 80))
    temperatureText = Text(font_path, 24, '天氣狀況:'+temperature,
                           (255, 255, 255), (20, 110))

    # Game Loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type in event_handlers:
                event_handlers[event.type]()

        if running:
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

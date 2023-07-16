import pygame
from modules.input_handler import handle_input
from objects.Button import Button
from objects.Text import Text
from objects.Image import Image

# Setup 
window_width = 1280
window_height = 720
running = True
dt = 0

pygame.init()

screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()


# Event Handlers
def handle_quit_event():
    pygame.quit()

def handle_button_click():
    # 处理按钮点击事件的逻辑
    if button.check_collision(pygame.mouse.get_pos()):
        text.set_text("Lalala") # 当按钮与鼠标点击位置发生碰撞时执行相应逻辑

# Events
event_handlers = { 
    pygame.QUIT: handle_quit_event,
    pygame.MOUSEBUTTONDOWN: handle_button_click
}

# Game Created
logo_image = Image("images/pygame_lofi.png",100,100)
button = Button("images/button.png",(window_width/2, window_height - 100))
text = Text(None, 36, "AAA",  (255, 255, 255), (window_width // 2, 20))
player_pos = pygame.Vector2(screen.get_width() // 2, screen.get_height() // 2)
screen.fill("gray")

# Game Loop
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type in event_handlers:
            event_handlers[event.type]()

    # 更新
    screen.fill("gray")
    button.draw(screen)
    text.draw(screen)
    logo_image.draw(screen)


    # 移動
    handle_input(player_pos, dt)
    pygame.draw.circle(screen, "yellow", player_pos, 40)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()

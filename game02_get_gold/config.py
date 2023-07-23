
import os


IMAGE_PATHS = {
    'gold': os.path.join(os.getcwd(), 'game02_get_gold/resources/images/gold.png'),
    'apple': os.path.join(os.getcwd(), 'game02_get_gold/resources/images/apple.png'),
    'background': os.path.join(os.getcwd(), 'game02_get_gold/resources/images/8bit-background.webp'),
    'hero': [os.path.join(os.getcwd(), 'game02_get_gold/resources/images/%d.png' % i) for i in range(1, 11)]
}

AUDIO_PATHS = {
    'bgm': os.path.join(os.getcwd(), 'game02_get_gold/resources/audios/bgm.mp3'),
    'get': os.path.join(os.getcwd(), 'game02_get_gold/resources/audios/get.wav'),
}

FONT_PATH = os.path.join(os.getcwd(), 'common/fonts/NotoSansTC-Bold.otf')

HIGHEST_SCORE_RECORD_FILEPATH = 'highest.rec'

SCREENSIZE = (800, 600)

BACKGROUND_COLOR = (0, 160, 233)

FPS = 30

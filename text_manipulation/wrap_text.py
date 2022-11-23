import pygame as pg
from string import printable
from math import log

WHITE = 255, 255, 255
RED = 255, 0, 0
ORANGE = 255, 180, 0
YELLOW = 255, 255, 0
GREEN = 0, 200, 0
BLUE = 0, 0, 255
VIOLET = 143, 0, 255
GREY = 150, 150, 150
BLACK = 0, 0, 0


def text(msg: str, x, y, fg=GREEN):
    text_sur = font.render(str(msg), True, fg)
    text_rect = text_sur.get_rect()
    text_rect.center = x, y
    screen.blit(text_sur, text_rect)


def wrap_text(msg, x, y):
    lines = [""]
    for char in str(msg):
        if font.size(char + lines[-1])[0] >= WIDTH:
            lines.append(char)
        else:
            lines[-1] += char
    for i, line in enumerate(lines):
        text(line, x, y + font.get_height() * (i))  # - len(lines) / 2))


pg.init()
font = pg.font.SysFont("Arial", 40)
screen = pg.display.set_mode((1080, 2044))
clock = pg.time.Clock()
WIDTH, HEIGHT = screen.get_size()

i = 2 * 39**20
while True:
    screen.fill(BLACK)
    wrap_text(i, WIDTH / 2, 25)  # HEIGHT / 2)
    i *= 39
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    pg.display.update()
    clock.tick(10)

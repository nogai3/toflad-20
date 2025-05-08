from util import Colors
from util.input import KeyboardInput as keyboard
from util.input import MouseInput as mouse
from util.sound import Sound as sound
from util.timer import Ticks
from engine.controls import Controls as control
from engine.commands import Commands as cmd
from engine.logger import Logger as log
from sprites import Test
import pygame as pg
pg.init()

widthDefault = 1280; heightDefault = 720; currentWidth = 0; currentHeight = 0
window = pg.display.set_mode([widthDefault, heightDefault])

def Start(title, width, height, defaultColor, fps):
    global window, currentWidth, currentHeight
    window = pg.display.set_mode([width, height])
    currentWidth = width; currentHeight = height
    pg.display.set_caption(title)
    window.fill(defaultColor)

    begin_play()

    pg.display.flip()
    gameTitle = title
    running = True
    while running:
        tick()
        Ticks.ticks(fps)
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                running = False
    pg.quit()
def begin_play():
    Test.draw()
    log.create_log_file("test.log")
def tick():
    control.Controls()
    log.write_in_log_file("test.log", "", f"MousePos (X, Y): {mouse.mouse_pos}", "0")
def get_width(): return currentWidth
def get_height(): return currentHeight
def fill_window(color): window.fill(color)
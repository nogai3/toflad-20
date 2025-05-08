from util import Colors
from util.input import KeyboardInput
from util.input import MouseInput
from util.sound import Sound
from util.timer import Ticks
from engine.controls import Controls
from engine.commands import Commands
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

    beginPlay()

    pg.display.flip()
    gameTitle = title
    running = True
    while running:
        tick()
        Controls.controls()
        Ticks.ticks(fps)
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                running = False
    pg.quit()

def beginPlay():
    a = 2
def tick():
    a = 1
    
def getWidth(): return currentWidth
def getHeight(): return currentHeight
def fillWindow(color): window.fill(color)
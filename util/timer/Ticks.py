import pygame as pg

clock = pg.time.Clock()

def ticks(ticks):
    global clock
    return clock.tick(ticks)
def get_FPS():
    global clock
    return clock.get_fps()
def wait(seconds):
    pg.time.wait(int(seconds * 1000))
def delay(seconds):
    pg.time.delay(int(seconds * 1000))

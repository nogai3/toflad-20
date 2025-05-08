import pygame as pg

keys_down = set()
keys_up = set()
keys_held = set()

def read():
    global keys_down, keys_up, keys_held
    keys_down.clear()
    keys_up.clear()

    for event in pg.event.get():
        match (event.type):
            case pg.QUIT:
                pg.quit()
            case pg.KEYDOWN:
                keys_down.add(event.key)
            case pg.KEYUP:
                keys_up.add(event.key)
    pressed = pg.key.get_pressed()
    keys_held.clear()
    for keycode in range(len(pressed)):
        if (pressed[keycode]):
            keys_held.add(keycode)
def update():
    return {
        "down": keys_down.copy(),
        "up": keys_up.copy(),
        "held": keys_held.copy()
    }
def clear():
    keys_down.clear()
    keys_up.clear()
    keys_held.clear()

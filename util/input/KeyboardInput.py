import pygame as pg

keysDown = set()
keysUp = set()
keysHeld = set()

def read():
    global keysDown, keysUp, keysHeld
    keysDown.clear()
    keysUp.clear()

    for event in pg.event.get():
        match (event.type):
            case pg.QUIT:
                pg.quit()
            case pg.KEYDOWN:
                keysDown.add(event.key)
            case pg.KEYUP:
                keysUp.add(event.key)
    pressed = pg.key.get_pressed()
    keysHeld.clear()
    for keycode in range(len(pressed)):
        if (pressed[keycode]):
            keysHeld.add(keycode)
def update():
    return {
        "down": keysDown.copy(),
        "up": keysUp.copy(),
        "held": keysHeld.copy()
    }
def clear():
    keysDown.clear()
    keysUp.clear()
    keysHeld.clear()

import pygame as pg

mouseButtonsDown = set()
mouseButtonsUp = set()
mouseButtonsHeld = set()

mousePos = (0, 0)
mouseRel = (0, 0)
mouseWheel = 0

def read():
    global mouseButtonsDown, mouseButtonsUp, mouseButtonsHeld
    global mousePos, mouseRel, mouseWheel

    mouseButtonsDown.clear()
    mouseButtonsUp.clear()
    mouseWheel = 0

    mousePos = pg.mouse.get_pos()
    mouseRel = pg.mouse.get_rel()

    for event in pg.event.get([pg.MOUSEBUTTONDOWN, pg.MOUSEBUTTONUP, pg.MOUSEWHEEL]):
        match (event.type):
            case pg.MOUSEBUTTONDOWN:
                mouseButtonsDown.add(event.button)
            case pg.MOUSEBUTTONUP:
                mouseButtonsUp.add(event.button)
            case pg.MOUSEWHEEL:
                mouseWheel += event.y
    pressed = pg.button.get_pressed()
    mouseButtonHeld.clear()
    for keycode in range(len(pressed)):
        if (pressed[keycode]):
            mouseButtonsHeld.add(keycode)
def update():
    return {
        "down": mouseButtonsDown.copy(),
        "up": mouseButtonsUp.copy(),
        "held": mouseButtonsHeld.copy(),
        "pos": mousePos,
        "rel": mouseRel,
        "wheel": mouseWheel
    }
def clear():
    mouseButtonsDown.clear()
    mouseButtonsUp.clear()
    mouseButtonsHeld.clear()
    
    mousePos = (0, 0)
    mouseRel = (0, 0)
    mouseWheel = 0
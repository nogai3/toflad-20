import pygame as pg

mouse_buttons_down = set()
mouse_buttons_up = set()
mouse_buttons_held = set()

mouse_pos = (0, 0)
mouse_rel = (0, 0)
mouse_wheel = 0

def read():
    global mouse_buttons_down, mouse_buttons_up, mouse_buttons_held
    global mouse_pos, mouse_rel, mouse_wheel

    mouse_buttons_down.clear()
    mouse_buttons_up.clear()
    mouse_wheel = 0

    mouse_pos = pg.mouse.get_pos()
    mouse_rel = pg.mouse.get_rel()

    for event in pg.event.get([pg.MOUSEBUTTONDOWN, pg.MOUSEBUTTONUP, pg.MOUSEWHEEL]):
        match (event.type):
            case pg.MOUSEBUTTONDOWN:
                mouse_buttons_down.add(event.button)
            case pg.MOUSEBUTTONUP:
                mouse_buttons_up.add(event.button)
            case pg.mouse_wheel:
                mouse_wheel += event.y
    pressed = pg.mouse.get_pressed()
    mouse_buttons_held.clear()
    for keycode in range(len(pressed)):
        if (pressed[keycode]):
            mouse_buttons_held.add(keycode)
def update():
    return {
        "down": mouse_buttons_down.copy(),
        "up": mouse_buttons_up.copy(),
        "held": mouse_buttons_held.copy(),
        "pos": mouse_pos,
        "rel": mouse_rel,
        "wheel": mouse_wheel
    }
def clear():
    mouse_buttons_down.clear()
    mouse_buttons_up.clear()
    mouse_buttons_held.clear()
    
    mouse_pos = (0, 0)
    mouse_rel = (0, 0)
    mouse_wheel = 0
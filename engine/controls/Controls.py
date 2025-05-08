from util.input import KeyboardInput as keyboard
from util.input import MouseInput as mouse
import pygame as pg

def Controls():
    keyboard.read()
    mouse.read()
    state = keyboard.update()
    mouse_state = mouse.update()

    key_map = {
        pg.K_w: "forward",
        pg.K_s: "backward",
        pg.K_a: "left",
        pg.K_d: "right"
    }

    for key, direction in key_map.items():
        if (key in state["down"] or state["held"] or state["up"]):
            print(state)
    
    if (1 in mouse_state["up"] or mouse_state["held"] or mouse_state["down"]):
        print(f"LMB is {mouse_state}")
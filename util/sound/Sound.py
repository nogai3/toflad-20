import pygame as pg

def play_music(path):
    pg.mixer.music.load(path)
    pg.mixer.music.play()
def play_sound(path):
    pg.mixer.sound(path).play()
import pygame as pg

def playMusic(path):
    pg.mixer.music.load(path)
    pg.mixer.music.play()
def playSound(path):
    pg.mixer.sound(path).play()
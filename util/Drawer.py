import pygame as pg

def drawCircle(window, color, pos, radius, fill):
    pg.draw.circle(window, color, pos, radius, fill)
def drawLine(window, color, start, end, width):
    pg.draw.line(window, color, start, end, width)
def drawRect(window, color, size, width):
    pg.draw.rect(window, color, size, width)
def loadImage(path):
    pg.image.load(image)
def renderImage(window, image, x, y):
    window.blit(image, (x, y))
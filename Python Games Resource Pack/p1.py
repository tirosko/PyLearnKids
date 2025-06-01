import pygame
import pgzrun
import pgzero
from pgzero import screen


def draw():
    screen.clear()
    screen.draw.text("Hello, Pygame Zero!", (50, 50))


pgzrun.go()

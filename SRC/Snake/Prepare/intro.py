import pgzrun
from pgzero import screen
# This is a simple Pygame Zero program that draws a red rectangle and prints the mouse click position
WIDTH = 300
HEIGHT = 300


def draw():
    screen.fill((128, 0, 0))
    screen.draw.rect((0, 0, WIDTH, HEIGHT), (255, 0, 0))
    screen.draw.text("Click anywhere", (10, 10), color=(255, 255, 255))

# importing the module
import pygame
# importing the module
import random

# instantiating the class
pygame.init()

# dimension of the screen
width = 700
height = 550

# colours
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
clk = pygame.time.Clock()  # clock

# creating a Screen
screen = pygame.display.set_mode((width, height))

# title of the screen
pygame.display.set_caption("Bouncy Ball")

# 2 krok - vytvorenie lopty

# declaring variables for the ball
ball_X = width/2 - 12
ball_Y = height/2 - 12
ball_XChange = 3 * random.choice((1, -1))
ball_YChange = 3
ballPixel = 24

# 3 krok - slučka programu
# gaming Loop
running = True
while running:

    # background color
    screen.fill(red)

    # to exit the loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# 4 krok - podmienka pre hranicu
# inside the gaming Loop

    # bouncing the ball
    if ball_X + ballPixel >= width or ball_X <= 0:
        ball_XChange *= -1
    if ball_Y + ballPixel >= height or ball_Y <= 0:
        ball_YChange *= -1

    # moving the ball
    ball_X += ball_XChange
    ball_Y += ball_YChange

# 5 krok - kreslenie loptičky
# inside the gaming Loop

    # drawing the ball
    ballImg = pygame.draw.circle(screen, (0, 0, 255),
                                 (int(ball_X), int(ball_Y)),
                                 15)
    clk.tick(60)
    pygame.display.update()
